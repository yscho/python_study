import os


class cDefaultPathControl():

    src_path_filenmae = "./src_default_path.bin"
    tar_parh_filename = "./tar_default_path.bin"
    temp_path = "test"

    def init_src_tar_path_txt(self, argobj_line_Edit_tar ,argobj_line_Edit_src ):

        print("init_src_tar_path_txt")
        if os.path.exists(self.src_path_filenmae):
            self.load_path("tar")
            print("---" + self.temp_path)
            argobj_line_Edit_tar.setText(self.temp_path)
            self.load_path("src")
            print("---" + self.temp_path)
            argobj_line_Edit_src.setText(self.temp_path)

    def save_path(self, src_tar, full_path):
        print("save_path "+src_tar)
        if src_tar == "src":
            f = open("./src_default_path.bin", 'w')
            f.write(full_path)
            f.close()
        elif src_tar == "tar":
            f = open("./tar_default_path.bin", 'w')
            f.write(full_path)
            f.close()
        else:
            print("err : src")

    def load_path(self, src_tar):
        if src_tar == "src":
            f = open("./src_default_path.bin", 'r')
            self.temp_path = f.readline()
            print(self.temp_path)
            f.close()

        elif src_tar == "tar":
            f = open("./tar_default_path.bin", 'r')
            self.temp_path = f.readline()
            print(self.temp_path)
            f.close()
        else:
            print("err : src")
