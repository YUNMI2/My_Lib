import write_file
class ReadFile:
    def readMDBfile(self,file_name = ""):
        '''
        :function 读取一个文件夹下面的MDB文件(数据库文件)
        :param file_name:文件夹名
        :return:
        '''
        dict_list = []
        if file_name == "":
            print("the file path is  not correct! ")
            return []
        else:
            import win32com.client
            conn = win32com.client.gencache.EnsureDispatch('ADODB.Connection')
            DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = %s'%(file_name)
            conn.Open(DSN)
            rs = win32com.client.Dispatch('ADODB.Recordset')
            rs.Open ("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0", conn, 1,3)#获取所有表名
            table_list = []
            rs.MoveFirst()
            while not rs.EOF:
                for x in range(rs.Fields.Count):
                    table_list.append(rs.Fields.Item(x).Value)
                rs.MoveNext()
            for one_table_name in table_list:
                print("table_name: " ,one_table_name)
                ro = win32com.client.Dispatch('ADODB.Recordset')
                ro.Open('[' + one_table_name + ']', conn, 1, 3)
                ro.MoveFirst()
                while not ro.EOF:
                    dict_one = {}
                    dict_one["table_name"] = one_table_name
                    for x in range(ro.Fields.Count):
                        dict_one[ro.Fields.Item(x).Name] = ro.Fields.Item(x).Value
                        # print(ro.Fields.Item(x).Name ,end= ":")
                        # print(ro.Fields.Item(x).Value,end = "\t")
                    # print("\n")
                    dict_list.append(dict_one)
                    ro.MoveNext()
                print(len(dict_list))
            conn.Close()
            return dict_list




if __name__ == "__main__":
    my_test = ReadFile()
    dict_list = my_test.readMDBfile("word_seg_peking.mdb")
    if dict_list == []:
        exit()

    write_file_test = write_file.WriteFile()
    write_file_test.write_list_to_json_file("peking_seg_corpus.json", dict_list)



