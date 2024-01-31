import csv
import requests
import fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]