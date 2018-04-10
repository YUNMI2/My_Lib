import write_file
class ReadFile:
    def readMDBfile_back_complex_dict(self,file_name = ""):
        '''
        :function 读取一个文件夹下面的MDB文件(数据库文件)
        :param file_name:文件夹名
        :return:complex_dict：key1:表名
                                key1.key:id
                                key1.value:record
        '''
        dict_all = {}
        if file_name == "":
            print("the file path is  not correct! ")
            return {}
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
                    dict_all[rs.Fields.Item(x).Value] = {}
                rs.MoveNext()
            for one_table_name in table_list:
                ro = win32com.client.Dispatch('ADODB.Recordset')
                ro.Open('[' + one_table_name + ']', conn, 1, 3)
                ro.MoveFirst()

                id = 0
                while not ro.EOF:
                    dict_one = {}
                    dict_one["id"] = id
                    dict_one["table_name"] = one_table_name
                    for x in range(ro.Fields.Count):
                        dict_one[ro.Fields.Item(x).Name] = ro.Fields.Item(x).Value

                    dict_all[one_table_name][id] = dict_one
                    ro.MoveNext()
                    id += 1
            conn.Close()
            return dict_all

    def readMDBfile_back_simple_dict(self,file_name = ""):
        '''
        :function 读取一个文件夹下面的MDB文件(数据库文件)
        :param file_name:文件夹名
        :return:一层的dict:key为id，value为记录
        '''
        dict_all = {}
        if file_name == "":
            print("the file path is  not correct! ")
            return {}
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
                    # dict_all[rs.Fields.Item(x).Value] = {}
                rs.MoveNext()
            all_id = 0
            for one_table_name in table_list:
                ro = win32com.client.Dispatch('ADODB.Recordset')
                ro.Open('[' + one_table_name + ']', conn, 1, 3)
                ro.MoveFirst()
                id = 0
                while not ro.EOF:
                    dict_one = {}
                    dict_one["id"] = id
                    dict_one["table_name"] = one_table_name
                    for x in range(ro.Fields.Count):
                        if ro.Fields.Item(x).Value != None:
                            dict_one[ro.Fields.Item(x).Name] = ro.Fields.Item(x).Value

                    dict_all[all_id] = dict_one
                    ro.MoveNext()
                    id += 1
                    all_id += 1
            conn.Close()
            return dict_all


    def readMDBfile_back_all_attribute_dict(self,file_name = ""):
        '''
        :function 读取一个文件夹下面的MDB文件(数据库文件)
        :param file_name:文件夹名
        :return:一层的dict:key为id，value为记录
        '''
        dict_all = {}
        if file_name == "":
            print("the file path is  not correct! ")
            return {}
        else:
            attribute_list = []
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
                ro = win32com.client.Dispatch('ADODB.Recordset')
                ro.Open('[' + one_table_name + ']', conn, 1, 3)
                for x in range(ro.Fields.Count):
                    if ro.Fields.Item(x).Name not in attribute_list:
                        attribute_list.append(ro.Fields.Item(x).Name)
            conn.Close()
            for i in range(len(attribute_list)):
                dict_all[i] = attribute_list[i]
            return dict_all



    def readMDBfile_back_list(self, file_name=""):
        '''
        :function 读取一个文件夹下面的MDB文件(数据库文件)
        :param file_name:文件夹名
        :return:dict_list
        '''
        dict_list = []
        if file_name == "":
            print("the file path is  not correct! ")
            return []
        else:
            import win32com.client
            conn = win32com.client.gencache.EnsureDispatch('ADODB.Connection')
            DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = %s' % (file_name)
            conn.Open(DSN)
            rs = win32com.client.Dispatch('ADODB.Recordset')
            rs.Open("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0", conn, 1, 3)  # 获取所有表名
            table_list = []
            rs.MoveFirst()
            while not rs.EOF:
                for x in range(rs.Fields.Count):
                    table_list.append(rs.Fields.Item(x).Value)
                rs.MoveNext()
            for one_table_name in table_list:
                print("table_name: ", one_table_name)
                ro = win32com.client.Dispatch('ADODB.Recordset')
                ro.Open('[' + one_table_name + ']', conn, 1, 3)
                ro.MoveFirst()
                while not ro.EOF:
                    dict_one = {}
                    dict_one["table_name"] = one_table_name
                    for x in range(ro.Fields.Count):
                        dict_one[ro.Fields.Item(x).Name] = ro.Fields.Item(x).Value
                    dict_list.append(dict_one)
                    ro.MoveNext()
            conn.Close()
            return dict_list



    def readJsonfile(self,file_name):
        Json_dict = {}
        if file_name != "":
            import json
            with open(file_name, "r", encoding = "utf-8") as fo:
                Json_dict = json.load(fo)
        return Json_dict







if __name__ == "__main__":
    test = ReadFile()
    all_dict = test.readMDBfile_back_simple_dict("word_seg_peking.mdb")
    all_att_dict = test.readMDBfile_back_all_attribute_dict("word_seg_peking.mdb")
    if all_dict == {}:
        exit()
    import write_file
    Writer = write_file.WriteFile()
    Writer.write_json_file("peking_seg_corpus.json",all_dict)
    Writer.write_json_file("peking_seg_corpus_all_attribute.json",all_att_dict)

