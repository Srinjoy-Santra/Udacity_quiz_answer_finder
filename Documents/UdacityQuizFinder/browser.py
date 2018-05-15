import webbrowser
import subprocess
import pyperclip as pc

import requests
import bs4


def reference():
    string = '''
    
    '''


def comment():
    string = '''Hope it helps :smile:
Leave A Like If That Helped You Out :+1: Thank You :smile:'''


def lesson_url(x):
    return {
        2: 'https://classroom.udacity.com/courses/ud304-in/lessons/6987421963/concepts/',
        5: 'https://classroom.udacity.com/courses/ud304-in/lessons/7473321627/concepts/',
        6: 'https://classroom.udacity.com/courses/ud304-in/lessons/7323812069/concepts/',
        11: 'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/',
        12: 'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/',
        13: 'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/',
        14: 'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/',
        15: 'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/',
        16: 'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/',
        18: 'https://classroom.udacity.com/courses/ud304-in/lessons/3314378535/concepts/',
        19: 'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/',
        20: 'https://classroom.udacity.com/courses/ud304-in/lessons/5103579406/concepts/'

    }.get(x, 'Not found')


def modified_quiz(x):
    return {
        5: 0,
        6: 1,
        11: 2,
        12: 3,
        13: 4,
        14: 5,
        15: 6,
        16: 7,
        18: 8,
        19: 9,
        20: 10,
        2: 11




    }.get(x, 'Not found')

    '''    if x is 5:
        return x - 5
    elif x is 6:
        return x - 5
    elif x is 18:
        return x - 10
    elif x is 19:
        return x - 10
    elif x is 2:
        return 11;
    else:
        return x - 9'''



# Find the right link to udacity answers
# webbrowser.open("'https://reekcrazy.wordpress.com/", 2)

# help(webbrowser)

# chrome = webbrowser.get(using=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s").open("'https://reekcrazy.wordpress.com/")
# webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

if __name__ == '__main__':

    quiz_list = [
        # css urls

        #  5
        ['74280262920923',
         '74276264140923',
         '74276264170923',
         '74790318980923',
         '74276264210923',
         '74276264250923',
         '74276264290923',
         '74276264330923'],

        # 6
        ['71153997690923',
         '71213796920923',
         '73294517320923',
         '71182299710923',
         '75533070630923',
         ],

        # javascript urls /0ea84522-b154-482c-a51f-c8d13e8dce63
        # 11 Datatypes and variables
        [
            '0ea84522-b154-482c-a51f-c8d13e8dce63',
            '5f0a00eb-e0c7-4b3f-a24d-400cad12176e',
            '57b2d4f9-c79a-45dd-898f-ac62440d882b',
            '1094e5d1-4986-42e5-9777-fa43d269ec81',
            '5a82b56c-8c1e-40e4-acc9-cc396fbfb439',
            '69fa04db-4a01-443b-89f5-e60626379ef9',
            '071e3541-983b-4dae-9f60-cb89d362b640',
            '2c5e7a00-fdb9-4617-828f-5c870da31636',
            'bbd404b6-2d49-4c9c-9606-e0bc5ca1e224',
            'fd9cb0be-5118-4855-ac43-d37a34be8709',
            '03beabe9-bc85-4fab-9af2-909321e8e416',
            '3c43abc9-d9c6-4e55-bceb-08b119fff788'
        ]
        ,
        # 12 Conditionals
        [
            '5884611b-3df7-46f8-9ab7-1dcae8a88e5c',
            'd390c340-06f3-4da3-a202-3d38d671408b',
            '5c45f6af-cdbb-42a9-a0a1-8e33dedbfc9f',
            'e09da5d2-9a1e-40d6-bcd2-99078b263110',
            '03d8062f-6e1f-4f79-86e5-f49cde75e36d',
            'b651694a-cfda-4965-be84-279387f32c44',
            '1c7f869b-60fd-4746-a90e-5287f4a473dc',
            '0dccb26f-7a9e-465e-a2e7-5362c3e278e6'
        ],
        # 13 Loops
        [
            '2a571380-d3dc-4acb-98a1-96766e6d5436',
            'd150e73c-6439-461e-b52b-87c6e5c1ea3a',
            'e2383410-4647-455e-92aa-f495c2753a08',
            'ed32a833-056e-48df-9523-2dd5f57b31b9',
            '54374289-dc31-4c28-bca5-a1d964e4b343',
            'dd074394-243a-4467-babf-14563c6b8c71',
            '371cff31-42a7-4e5e-93e2-f0c3dd5cc7d0',
            '4999de08-ae90-41d0-bbe4-526161faee74'
        ],
        # 14 Functions
        [
            'fb73adf6-2822-472f-a6af-3af6c29d7fdd',
            'fb73adf6-2822-472f-a6af-3af6c29d7fdd',
            'c746623a-eefd-4518-9890-2c5f320b0282',
            '61f50acf-0bc9-4195-adda-c46d8222fe5b',
            '807696ab-6a0d-4bf7-a2ee-8f5786ea1587',
            '3d40a839-ffaa-4a34-bb10-bec27b23e1c6'
        ],
        # 15 Arrays
        [
            'c7572c91-7faa-4f14-8e77-884ccc469883',
            'cb825759-f27d-4a88-90a7-032a1ea4bc09',
            '50758680-b82e-413e-8ac8-cc7dd006d435',
            'fac8e631-f0e4-46d5-8b24-1b5df5f2bffc',
            '2ddb79f7-d339-482e-a136-a25ef430f597',
            'b9d9a6fa-549e-4b97-867e-142f386e3711',
            '5c23d91d-3125-4887-8076-bd7d34c04953',
            '4c880baa-e51b-4b8e-bea0-50c5849688dd',
            'fc5ae6f0-2cf3-4e44-a1dc-4df1e66a7ddb',
            '037baa90-8a32-414b-a801-1d45dce44874'
        ],
        # 16 objects
        [
            '808f82c1-da3c-4e6d-ac94-76ce4193cbbb',
            '89c6f0dc-60e9-45f8-ba79-24f8922c8216',
            'a35ae1dd-3f00-4798-8983-a43b4b5ad589',
            'c80dc57a-dbe8-49c2-b018-0435c4b7142b',
            '104ab221-418a-4e72-9086-9f9332cc2d05',
            '27843aa3-2082-4f21-b465-d594f95af9e1'
        ],
        # $ jdom
        # 18 basics
        ['33166386840923',
         '33166386890923',
         '33166386930923',
         '33166386960923',
         '33166386960923',
         '33166387030923']
        ,
        # 19 DOM manip
        ['33271685970923',
         '33240785570923',
         '33271686010923',
         '33271686040923',
         '33271686080923',
         '33271686110923',
         '33271686160923',
         '33271686190923',
         '33271686220923'],

        # 20 event listeners
        ['50676237180923',
         '50676237240923',
         '50676237270923',
         '50676237290923'
         ],

        #  2 html syntax
        ['74229205910923',
         '74229205980923',
         '74229206010923'
         ]
    ]

    lesson = int(input('lesson='))
    if lesson is not 4 and lesson is not 8:
        quiz = int(input('Choose between(1,' + str(len(quiz_list[modified_quiz(lesson)])) + ') quiz='))
    # index = int(input('index'))
    if lesson is 4:
        subprocess.Popen(
            r'explorer /select, "C:\Users\nEW u\Documents\UdacityFreeScholarship\mockup-to-article\mockup-to-article"')
    elif lesson is 8:
        subprocess.Popen(
            r'explorer /select, "C:\Users\nEW u\Documents\UdacityFreeScholarship\fend-animal-trading-cards-master"')
    else:

        # normal js course 11=2!!

        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s") \
            .open(lesson_url(lesson) + quiz_list[modified_quiz(lesson)][quiz - 1])

    pc.copy(comment())
'''


11
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/0ea84522-b154-482c-a51f-c8d13e8dce63',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/5f0a00eb-e0c7-4b3f-a24d-400cad12176e',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/57b2d4f9-c79a-45dd-898f-ac62440d882b',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/1094e5d1-4986-42e5-9777-fa43d269ec81',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/5a82b56c-8c1e-40e4-acc9-cc396fbfb439',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/69fa04db-4a01-443b-89f5-e60626379ef9',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/071e3541-983b-4dae-9f60-cb89d362b640',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/2c5e7a00-fdb9-4617-828f-5c870da31636',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/bbd404b6-2d49-4c9c-9606-e0bc5ca1e224',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/fd9cb0be-5118-4855-ac43-d37a34be8709',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/03beabe9-bc85-4fab-9af2-909321e8e416',
'https://classroom.udacity.com/courses/ud304-in/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/3c43abc9-d9c6-4e55-bceb-08b119fff788


12
'5884611b-3df7-46f8-9ab7-1dcae8a88e5c',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/d390c340-06f3-4da3-a202-3d38d671408b',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/5c45f6af-cdbb-42a9-a0a1-8e33dedbfc9f',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/e09da5d2-9a1e-40d6-bcd2-99078b263110',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/03d8062f-6e1f-4f79-86e5-f49cde75e36d',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/b651694a-cfda-4965-be84-279387f32c44',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/1c7f869b-60fd-4746-a90e-5287f4a473dc',
'https://classroom.udacity.com/courses/ud304-in/lessons/3ace947b-b5f6-40c1-bc11-3ec98fd1d936/concepts/0dccb26f-7a9e-465e-a2e7-5362c3e278e6


13
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/2a571380-d3dc-4acb-98a1-96766e6d5436',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/d150e73c-6439-461e-b52b-87c6e5c1ea3a',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/e2383410-4647-455e-92aa-f495c2753a08',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/ed32a833-056e-48df-9523-2dd5f57b31b9',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/54374289-dc31-4c28-bca5-a1d964e4b343',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/dd074394-243a-4467-babf-14563c6b8c71',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/371cff31-42a7-4e5e-93e2-f0c3dd5cc7d0',
'https://classroom.udacity.com/courses/ud304-in/lessons/1234cec0-179b-40b6-9435-f10263c7de33/concepts/4999de08-ae90-41d0-bbe4-526161faee74

14
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/fb73adf6-2822-472f-a6af-3af6c29d7fdd',
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/fb73adf6-2822-472f-a6af-3af6c29d7fdd',
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/c746623a-eefd-4518-9890-2c5f320b0282',
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/61f50acf-0bc9-4195-adda-c46d8222fe5b',
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/807696ab-6a0d-4bf7-a2ee-8f5786ea1587',
'https://classroom.udacity.com/courses/ud304-in/lessons/a7c5b540-51a6-44dc-b2f2-515c9dd6ca4f/concepts/3d40a839-ffaa-4a34-bb10-bec27b23e1c6

15
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/c7572c91-7faa-4f14-8e77-884ccc469883',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/cb825759-f27d-4a88-90a7-032a1ea4bc09',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/50758680-b82e-413e-8ac8-cc7dd006d435',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/fac8e631-f0e4-46d5-8b24-1b5df5f2bffc',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/2ddb79f7-d339-482e-a136-a25ef430f597',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/b9d9a6fa-549e-4b97-867e-142f386e3711',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/5c23d91d-3125-4887-8076-bd7d34c04953',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/4c880baa-e51b-4b8e-bea0-50c5849688dd',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/fc5ae6f0-2cf3-4e44-a1dc-4df1e66a7ddb',
'https://classroom.udacity.com/courses/ud304-in/lessons/378e7ff7-f7e5-4487-b5c4-fdf9b5c351d9/concepts/037baa90-8a32-414b-a801-1d45dce44874

16
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/808f82c1-da3c-4e6d-ac94-76ce4193cbbb',
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/89c6f0dc-60e9-45f8-ba79-24f8922c8216',
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/a35ae1dd-3f00-4798-8983-a43b4b5ad589',
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/c80dc57a-dbe8-49c2-b018-0435c4b7142b',
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/104ab221-418a-4e72-9086-9f9332cc2d05',
'https://classroom.udacity.com/courses/ud304-in/lessons/634eb53a-2f3f-47a3-9447-598090024758/concepts/27843aa3-2082-4f21-b465-d594f95af9e1

18
'https://classroom.udacity.com/courses/ud304-in/lessons/3314378535/concepts/33166386930923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3314378535/concepts/33166386960923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3314378535/concepts/33166386960923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3314378535/concepts/33166387030923'

19
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271685970923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33240785570923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686010923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686040923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686080923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686110923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686160923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686190923',
'https://classroom.udacity.com/courses/ud304-in/lessons/3311478538/concepts/33271686220923',




'''
