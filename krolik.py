from control import mous_control


def main():
    flag = 0
    while True:
        if flag==4:
            mous_control()
            flag=0
        flag +=1
        


if __name__ == "__main__":
    main() 
