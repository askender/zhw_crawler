# -*- coding:utf-8 -*-

from .base import BaseHandler
import requests
import json
import datetime
import utils


class ProjectHandler(BaseHandler):

    def get(self):
        project = self.get_argument('project', '')
        project_url = 'http://localhost:6800/listspiders.json?project=%s' % project
        jobs_url = 'http://localhost:6800/listjobs.json?project=%s' % project
        if project:
            running_spiders = []
            spiders = []
            try:
                r = requests.get(project_url, timeout=3)
            except requests.exceptions.RequestException as e:
                print(e)
            else:
                if r.status_code == requests.codes.ok:
                    spiders = r.json()['spiders']

            pending = running = finished = []
            try:
                r = requests.get(jobs_url, timeout=3)
            except requests.exceptions.RequestException as e:
                print(e)
            else:
                if r.status_code == requests.codes.ok:
                    res = json.loads(r.text)
                    pending = res['pending']
                    running = res['running']
                    finished = res['finished']

            s = ""
            s += "<table border='1'>"
            s += "<th>Project</th><th>Spider</th><th>Job</th><th>PID</th><th>Runtime</th><th>Log</th><th>Items</th>"
            s += "<tr><th colspan='7' style='background-color: #ddd'>Pending</th></tr>"
            for p in pending:
                s += "<tr>"
                s += "<td>%s</td>" % project
                for a in ['spider', 'id']:
                    s += "<td>%s</td>" % p[a]
                s += "<td></td>"
                s += "<td></td>"
                s += "</tr>"

            s += "<tr><th colspan='7' style='background-color: #ddd'>Running</th></tr>"
            for p in running:
                running_spiders.append(p['spider'])
                s += "<tr>"
                s += "<td>%s</td>" % project
                s += "<td>%s</td>" % p['spider']
                s += "<td>"
                s += p['id']
                s += '''<form action="/project" method="post">'''
                s += '''<input type='hidden' name='spider' value='%s'  />''' % p[
                    'spider']
                s += '''<input type='hidden' name='id' value='%s'  />''' % p[
                    'id']
                s += '''<input type='hidden' name='project' value='%s'  />''' % project
                s += '''<input type='hidden' name='action' value='stop'  />'''
                s += '''<input type='submit' value='stop'  />'''
                s += '''</form>'''
                s += "</td>"
                s += "<td></td>"
                s += "<td></td>"
                s += "</tr>"

            s += "<tr><th colspan='7' style='background-color: #ddd'>Finished</th></tr>"
            for p in finished:
                s += "<tr>"
                s += "<td>%s</td>" % project
                for a in ['spider', 'id']:
                    s += "<td>%s</td>" % p[a]
                s += "<td></td>"
                s += "<td>%s</td>" % (
                    datetime.datetime.strptime(p['end_time'],
                                               u"%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(p['start_time'],
                                                                                                     u"%Y-%m-%d %H:%M:%S.%f"))
                s += "<td><a href='http://localhost:6800/logs/%s/%s/%s.log'>Log</a></td>" % (
                    project, p['spider'], p['id'])
                s += "<td><a href='http://localhost:6800/items/%s/%s/%s.jl'>Items</a></td>" % (
                    project, p['spider'], p['id'])
                s += "</tr>"
            s += "</table>"

            job_num = {}
            for i in spiders:
                if not i.endswith('_local'):
                    job_num[i] = utils.get_job_num(i)

            self.render(
                'project.html',
                project=project,
                spiders=spiders,
                job_num=job_num,
                pending=pending,
                running=running,
                finished=finished,
                s=s,
            )
            return
        else:
            self.redirect('/view_crawler')

    def post(self):
        action = self.get_argument('action', '')
        project = self.get_argument('project', '')
        spider = self.get_argument('spider', '')
        job = self.get_argument('id', '')

        schedule_url = 'http://localhost:6800/schedule.json'
        cancel_url = 'http://localhost:6800/cancel.json'
        schedule_data = {'project': project, 'spider': spider}
        cancel_data = {'project': project, 'job': job}

        try:
            if action == 'start':
                r = requests.post(schedule_url, timeout=3, data=schedule_data)
            if action == 'stop':
                r = requests.post(cancel_url, timeout=3, data=cancel_data)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            if r and r.status_code == requests.codes.ok:
                pass
                # res = json.loads(r.text)
                # status = res['status']
                # print(status)

        self.redirect('/project?project=%s' % project)
