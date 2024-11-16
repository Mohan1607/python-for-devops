# store each and every line in variable 
# open file in write mode 
# update the configuration 
def update_conf(filepath, key, value):
    with open(filepath,"r") as file:
        lines=file.readlines()
    with open(filepath,"w") as file:
        for line in lines:
            if key in line:
                file.write(key+"="+value+"\n")
            else:
                file.write(line)

update_conf("server.conf","MAX_CONNECTIONS","700")
