import argparse
import logging


class Parser:
    #####Initialize the Arguemnts########
    def _initialize_parser(self):
        parser = argparse.ArgumentParser(
            "exec [--top10] [--persuccess] [--perfail] [--top10fail] [--top10hosts]")
        parser.add_argument("--top10", action="store_true", dest="top10",
                            help="1.  Top 10 requested pages and requests for each")
        parser.add_argument("--persuccess", action="store_true",
                            dest="persuccess", help="2.  Percentage of successful requests")
        parser.add_argument("--perfail", action="store_true", dest="perfail",
                            help="3.  Percentage of unsuccessful requests")
        parser.add_argument("--top10fail", action="store_true",
                            dest="top10fail", help="4.  Top 10 unsuccessful page requests")
        parser.add_argument("--top10hosts", action="store_true", dest="top10hosts",
                            help="5.  The top 10 hosts making the most requests")
        parser.add_argument("--all", action="store_true",
                            dest="all", help="6. The Complete reports")
        args = parser.parse_args()
        return args
