class Menu:
    is_open = True

    def set_openness(self, opening):
        if (opening):
            return self.try_open()
        else:
            return self.try_close()


    def try_open(self):
        if (not self.is_open):
            print("menu opened. waiting to close")
            self.is_open = True
            return "just opened"

    def try_close(self):
        if (self.is_open):
            print("menu closed. started waiting for dot")
            self.is_open = False
            return "just closed"