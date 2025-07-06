completed = 0

while completed < 100:
    completed += 10
    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break
        else:
            print("Remaining jumping jacks:", 100 - completed)
    else:
        print("Remaining jumping jacks:", 100 - completed)

    if completed == 100:
        print("Congratulations! You completed the workout.")
