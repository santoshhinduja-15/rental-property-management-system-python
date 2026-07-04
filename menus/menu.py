class Menu:
    @staticmethod
    def heading(title):

        print("\n" + "=" * 60)
        print(title.center(60))
        print("=" * 60)

    @staticmethod
    def pause():
        input("\nPress Enter to continue...")