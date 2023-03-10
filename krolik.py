from control import mous_control


def main():
<<<<<<< HEAD
    counter = 0
    while True:
        counter+=1
        if counter>3:
            mous_control()
            counter=0
=======
    flag = 0
    while True:
        if flag==4:
            mous_control()
            flag=0
        flag +=1
>>>>>>> fa95739 (0.0.2.2)
        


if __name__ == "__main__":
    main() 
