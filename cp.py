try:
    def cp():
        global b
        with open(r"/home/ubuntu/f1.txt","w") as i:
            i.write("hello this is my jenkins pipeline")
        with open(r"/home/ubuntu/f1.txt","r") as i:
            b=i.read()
        with open(r"/home/ubuntu/file2.txt","x") as i:
            i.write(b)
           # print("file data has been copy successfully by create mode !!!")
    
    ## calling the cp function
    cp()
except FileExistsError as i:
    with open(r"/home/ubuntu/file2.txt","a") as i:
        i.write(b)
        # print("File data has been copy successfully by append mode")
