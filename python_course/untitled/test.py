import requests
import time

ua_file1 = open("/Users/houyunlu/Desktop/work/code/copy_ua_template_param_leve1_leve2")
ua_file2 = open("/Users/houyunlu/Desktop/work/code/copy_ua_template_param_leve3_leve4")


def copy_ua(oldVersion, newVersion, oldAndNewLessonSns):
    url = "http://stage-internal-vk-l5d-as-3379.ua.vipkid-qa.com.cn/api/ua/template/batchCopy"

    payload = "{\"oldCurriculumVersion\":%s,\"newCurriculumVersion\":%s,\"oldAndNewLessonSns\":\"%s\"}" % (
    oldVersion, newVersion, oldAndNewLessonSns)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "bd948a47-5518-422f-a059-2b776c10620d"
    }
    print(payload)
    print(headers)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


# ua level1 level1=> version2->versionn1
oldAndNewLessonSns = ""
for line in ua_file1:
    line = line.strip()
    list = line.split()
    oldSn = list[0]
    newSn = list[1]
    oldAndNewLessonSns += oldSn + ':' + newSn + ','
print(oldAndNewLessonSns)
oldAndNewLessonSns = oldAndNewLessonSns[0:len(oldAndNewLessonSns) - 1]
print(oldAndNewLessonSns)
copy_ua(2, 1, oldAndNewLessonSns)
# ua level3 level4=> version1->versionn1
oldAndNewLessonSns = ""
for line in ua_file2:
    line = line.strip()
    list = line.split()
    oldSn = list[0]
    newSn = list[1]
    oldAndNewLessonSns += oldSn + ':' + newSn
print(oldAndNewLessonSns)
oldAndNewLessonSns = oldAndNewLessonSns[0:len(oldAndNewLessonSns) - 1]
print(oldAndNewLessonSns)
copy_ua(1, 1, oldAndNewLessonSns)