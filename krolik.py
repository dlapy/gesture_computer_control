from control import mous_control

def main():
    counter = 0
    while True:
        counter+=1
        if counter>3:
            mous_control()
            counter=0
        


if __name__ == "__main__":
    main() 
