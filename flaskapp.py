from flask import Flask
import jenkins
app = Flask(__name__)

server = jenkins.Jenkins('http://10.0.2.15:32000', username='admin', password='Mt8aVzeilEvbRgTu7dkiuk')
name = 'junit5-vanilla-maven/master'
jobs = server.get_jobs()
job1 = server.get_job_info(name)
builds = job1['builds']
time = 0
for build in builds:
     build = server.get_build_info(name, build['number'])
     build_time = build['duration']
     if build_time > time: #find which build is the longest 
        time = build_time
        build_num = build['number']
time_sec = int(time / 1000) #change time to sec

@app.route("/build")
def build_stat():
    return "Number of builds " + str(len(builds)) + "<br> Build #" + str(build_num) + " took the longest to run: " + str(time_sec) + " sceonds"

@app.route("/test")
def test_stat():
    return "Number of builds: " +str(len(builds)) + "<br> Build #5 had the longest running test <br> Test name: " + testname + "<br> Test duration: " + test_time
if __name__ == "__main__":
    app.run(debug=True)

