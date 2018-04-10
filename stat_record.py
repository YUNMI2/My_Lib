class Stat_Record:
    def stat_record_and_total_num(self,dict_all):
        """

        :param dict_all:复合字典
        :return:复合字典里面每个子字典的记录个数以及整个的记录个数
        """
        count_dict = {}
        if dict_all != {}:
            count_all = 0
            for key in dict_all:
                count_one = 0
                for key_2 in dict_all[key]:
                    count_one += 1
                count_dict[key] = count_one
                count_all += count_one
            count_dict["all"] = count_all
        return count_dict



if __name__ == "__main__":
    import read_file
    reader = read_file.ReadFile()
    dict_all = reader.readJsonfile("peking_seg_corpus.json")
    Stater = Stat_Record()
    count_all = Stater.stat_record_and_total_num(dict_all)
    import write_file
    Writer = write_file.WriteFile()
    Writer.write_json_file("count.json",count_all)

