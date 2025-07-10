students = {
    "Chinni" : {"math" : 90, "science" : 85, "physics" : 90, "beauty" : 90},
    "jashu" : {"math" : 85, "science" : 89, "physics" : 85, "beauty" : 98},
    "Dedee" : {"math" : 93, "science" : 91, "physics" : 88, "beauty" : 92}
}

lowest_phy = max(students.items(), key = lambda item : item[1]["beauty"])
print(f"Highest Marks scored Student: %s , HandsomeNess Score: %d", (lowest_phy[0], lowest_phy[1]['beauty']))   