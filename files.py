def read():
    numbers = []
    with open("Archivos/numbers.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    f.close()

def write():
    names = ["Jorge", "José", "Paco","Ignacio","Patricio","Marcos"]
    with open("Archivos/names.txt", "w",encoding="uft-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    f.close()

def run():
    write()

if __name__ == "__main__":
    run()