import sys

def main():
    if len(sys.argv)>1:
        for item in sys.argv[1:]:
            print("olá", item, "1")
    else:
        print("olá mundo!")

if __name__ == "__main__":
    main()