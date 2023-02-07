def main():
    ##################################################
    # Comlete your code here
    ##################################################
    male = int(input('Number of Males registered in the class: '))
    female = int(input('Number of Females registered in the class: '))
    total = int((male) + (female))
    malepercent = float(male/total)
    femalepercent = float(female/total)

    print ('The total number of students: ' + '\t\t{0}'. format(total))
    print ('The numbers of males and females: ' + '\t{0} \t\t{1}'. format (male, female))
    print ('The percentage of males and females: ' + '\t{0:.2f}% \t\t{1:.2f}%'. format(malepercent*100, femalepercent*100))
    pass


if __name__ == '__main__':
    main()
