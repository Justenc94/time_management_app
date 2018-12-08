d = {'key1': {5: 2}}

print(d)

d1 = {input("General category: "): {input('Category: '): {input('Sub-Category: '): input('Time elapsed: ')}}}

d.update(d1)

print(d)

taskDict = {'Productive': {'Reading': {'Poetry': 5000}},
            'Free-Time': {'Video Games': {'Ark': 2000}}}

print(taskDict)
print(taskDict['Productive']['Reading'])
#print(taskDict[input('First key: ')][input('Second key: ')])

for p_id, p_info in taskDict.items():
    print("\nGeneral Category:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])

