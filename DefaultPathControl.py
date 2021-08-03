import os


class cExplorerPathControl():

    src_path_filename = "./src_default_path.bin"
    tar_path_filename = "./tar_default_path.bin"
    default_path = "C:"
    temp_path = "test"

    def init_src_tar_path_txt(self, argobj_line_Edit_tar ,argobj_line_Edit_src ):

        print("init_src_tar_path_txt")
        self.load_path("tar")
        print("---" + self.temp_path)
        argobj_line_Edit_tar.setText(self.temp_path)
        self.load_path("src")
        print("---" + self.temp_path)
        argobj_line_Edit_src.setText(self.temp_path)


    def save_path(self, src_tar, full_path):
        print("save_path "+src_tar)
        if src_tar == "src":
            f = open(self.src_path_filename, 'w')
            f.write(full_path)
            f.close()
        elif src_tar == "tar":
            f = open(self.tar_path_filename, 'w')
            f.write(full_path)
            f.close()
        else:
            print("err : src")

    def load_path(self, src_tar):
        if src_tar == "src":
            if os.path.isfile(self.src_path_filename):
                f = open(self.src_path_filename, 'r')
                self.temp_path = f.readline()
                print(self.temp_path)
                f.close()
            else:
                self.temp_path = self.default_path
            return self.temp_path

        elif src_tar == "tar":
            if os.path.isfile(self.tar_path_filename):
                f = open(self.tar_path_filename, 'r')
                self.temp_path = f.readline()
                print(self.temp_path)
                f.close()
            else:
                self.temp_path = self.default_path
            return self.temp_path

        else:
            print("err : src")
