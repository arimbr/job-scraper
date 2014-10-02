import json

IN_FILE = 'items.json'
OUT_FILE = 'jobs.json'

# Merge two files
# checking that there are no duplicates ids
def merge(infile=IN_FILE, outfile=OUT_FILE):
    f2 = open(outfile)
    jobs = json.loads(f2.read())
    ids = [job['id'] for job in jobs]
    f2.close()

    f1 = open(infile)
    lines = f1.readlines()
    f1.close()

    count = 0
    for line in lines:
        job = json.loads(line.strip())
        if job['id'] not in ids:
            print job
            count += 1
            jobs.append(job)


    f2 = open(outfile, 'w')
    f2.write(json.dumps(jobs))

    print ""
    print "New jobs added: ", count

if __name__ == '__main__':
    merge(IN_FILE, OUT_FILE)
