import sys
from collections import Counter
from options import Parser

log_file = "access_log"


class Collector:

    def __init__(self, input_file=log_file):
        self.arg_parser = Parser()
        self.request_counter = 0
        self.line_number = 0
        self.success_counter = 0
        self.requested_url = Counter()
        self.unsuccessfull_reqst = Counter()
        self.top10hosts = Counter()
        self.top10hosts_dict = {}
        self.error_lines = {}
        self.input_file = input_file

    ########Top 10 requested URLs####################

    def requested_urls(self, line):
        # Capturing the URL and adding it to the Counter.
        try:
            self.requested_url[line.split()[6]] += 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"

    def top_ten_url(self):
        # Prining the Top ten with Counter most common option.
        top10requests = "----Top 10 requestsed URL----\n"
        for item in self.requested_url.most_common(10):
            top10requests += "URL : {0}  number of requests : {1}\n".format(
                item[0], item[1])
        return top10requests
    #################################################

    ##########Percentage of un|successful requests######
    def parse_successful_requests(self, line):
        # Counts the number of successful requests by reading 6th position of line
        try:
            status = line.split()[8]
            if int(status):
                if int(status) >= 200 and int(status) < 400:
                    self.success_counter += 1
        except ValueError:
            self.error_lines[self.line_number] = "malformed request: status is not an integer"
            self.request_counter -= 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1
        return self.success_counter
    ####################################################

    ############Top 10 unsuccessful page requests########
    def parse_unsuccessful_page_requests(self, line):
        # Counts the number of unsuccessful requested pages
        try:
            status = line.split()[8]
            if int(status):
                if int(status) >= 400:
                    self.unsuccessfull_reqst[line.split()[6]] += 1
        except ValueError:
            self.error_lines[self.line_number] = "malformed request: status is not an integer"
            self.request_counter -= 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1

    def top_ten_unsccessurl(self):
        # printing the URL with number of requests.
        top10unsuccessrequests = "----Top 10 unsuccessfull requestsed URL----\n"
        for item in self.unsuccessfull_reqst.most_common(10):
            top10unsuccessrequests += "URL : {0}  number of requests : {1}\n".format(
                item[0], item[1])
        return top10unsuccessrequests
    ###########################################################

    ############The top 10 hosts making the most requests and number of requests made########
    def parse_request_per_host(self, line):
        # Collects top 10 hosts and its top 5 requests
        try:
            host = line.split()[0]
            self.top10hosts[host] += 1
            if not self.top10hosts_dict:
                cnt = Counter()
                cnt[line.split()[6]] += 1
                self.top10hosts_dict.update({host: cnt})
            elif host in self.top10hosts_dict:
                value_cnt = self.top10hosts_dict[host]
                value_cnt[line.split()[6]] += 1
                self.top10hosts_dict.update(
                    {host: value_cnt})
            else:
                cnt = Counter()
                cnt[line.split()[6]] += 1
                self.top10hosts_dict.update({host: cnt})

        except Exception as e:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1

    def parse_top_ten_host(self):
        # print the outputs reports
        top10hosts = "----Top 10 hosts----\n"
        top5hostsrequest = "----Top 5 requests-----\n"
        for key, host in self.top10hosts.most_common(10):
            top10hosts += "host : {0} , Number of requests :  {1}\n".format(
                key, host)

        for key, host in self.top10hosts.most_common(10):
            if key in self.top10hosts_dict:
                top5hostsrequest += "host : {0} , Top 5 URL and number of requests :  {1}\n".format(
                    key, self.top10hosts_dict[key].most_common(5))
        return top10hosts, top5hostsrequest

    ###############################################################
    def collect_report(self):
        # Main function to Collects statistics and Produces Report
        self.parser = self.arg_parser._initialize_parser()
        with open(self.input_file) as logs:
            for line in logs.readlines():
                self.request_counter += 1
                self.line_number += 1
                if len(line.split()) < 10:
                    self.request_counter -= 1
                    self.error_lines[collector.line_number] = "malformed request, number of columns is not 10"
                    continue
                if self.parser.top10:
                    self.requested_urls(line)

                elif self.parser.persuccess or self.parser.perfail:
                    self.parse_successful_requests(line)

                elif self.parser.top10fail:
                    self.parse_unsuccessful_page_requests(line)

                elif self.parser.top10hosts:
                    self.parse_request_per_host(line)

                elif self.parser.all:
                    self.requested_urls(line)
                    self.parse_successful_requests(line)
                    self.parse_unsuccessful_page_requests(line)
                    self.parse_request_per_host(line)
            self.print_output()

    def print_output(self):
        # Print all the repors based on the arguments

        self.parser = self.arg_parser._initialize_parser()
        if self.parser.top10:
            print(self.top_ten_url())

        elif self.parser.persuccess:
            print("Percentage of successful requests: {0:.2f}".format(
                float(self.success_counter)/self.request_counter*100) + "\n")

        elif self.parser.perfail:
            self.failed_requests = int(
                self.request_counter - self.success_counter)
            print("Percentage of unsuccessful requests: {0:.2f}".format(
                float(self.failed_requests)/self.request_counter*100) + "\n")

        elif self.parser.top10fail:
            print(self.top_ten_unsccessurl())

        elif self.parser.top10hosts:
            x, y = self.parse_top_ten_host()
            print(x)
            print(y)

        elif self.parser.all:
            print(self.top_ten_url())
            print("Percentage of successful requests: {0:.2f}".format(
                float(self.success_counter)/self.request_counter*100) + "\n")
            self.failed_requests = int(
                self.request_counter - self.success_counter)
            print("Percentage of unsuccessful requests: {0:.2f}".format(
                float(self.failed_requests)/self.request_counter*100) + "\n")
            print(self.top_ten_unsccessurl())
            x, y = self.parse_top_ten_host()
            print(x)
            print(y)


if __name__ == "__main__":
    collector = Collector()
    collector.collect_report()
