import os
class WriteFile:
    def write_json_file(self,file_name,dict_one):
        if file_name == "":
            return
        else:
            import json
            with open(file_name, "w", encoding="utf-8",errors = "ignore") as fw:
                json.dump(dict_one,fw,indent=4,ensure_ascii=False)
                fw.write('\n')
                fw.flush()
                os.fsync(fw)

    def write_list_to_json_file(self,file_name,dict_list):
        if file_name == "":
            return
        else:
            import json
            print(len(dict_list))
            count = 0
            with open(file_name, "w", encoding="utf-8",errors = "ignore") as fw:
                for dict_one in dict_list:
                    count += 1
                    json.dump(dict_one,fw,indent=4,ensure_ascii=False)
                    fw.write('\n')

                fw.flush()
                os.fsync(fw)

    def write_list_to_txt_file(self,file_name,dict_list):
        if file_name == "":
            return
        else:
            import json
            with open(file_name, "w", encoding="utf-8",errors = "ignore") as fw:
                for dict_one in dict_list:
                    for k,v in dict_one.items():
                        fw.write(str(k) + ": " + str(v) + "")
                    fw.write('\n')
                fw.flush()
                os.fsync(fw)


if __name__ == "__main__":
    test = WriteFile()
    test.write_list_to_json_file("test.json",[{"a":1,"b":2},{"c":1,"d":2}])
