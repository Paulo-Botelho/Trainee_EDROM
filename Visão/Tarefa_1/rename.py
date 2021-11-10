import os

def main():
    for count, filename in enumerate(os.listdir("Imgs/")):
        
        dst ="robot" + str(count) + ".jpg"
        src ='Imgs/'+ filename
        dst ='imgs2/'+ dst

        os.rename(src, dst)



if __name__ == "__main__":
    main()