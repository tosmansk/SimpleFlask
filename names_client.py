import logging
logging.basicConfig(level=logging.DEBUG)
import requests, json


class MyLogger(object):
    """
    This calss sets logging
    """

    def __init__(self):
        super(MyLogger, self).__init__()
        self.log = logging.getLogger('LOGGER')


class NamesClient(MyLogger):

    def __init__(self, url):
        super(NamesClient, self).__init__()
        self.url = url

    def _prepare_url(self, suffix):
        return self.url.rstrip('/') + '/' + suffix.lstrip('/')

    def add_person(self, first_name, last_name):
        """
        This function adds entry of First and Last name to the server`s array data
        """

        url = self._prepare_url('/dodajNazwisko')
        self.log.info(url)
        post_data = {"FirstName" : first_name, "LastName" : last_name}
        response = requests.post(url,json=post_data)
        self.log.debug(response)
        return response.json()

    def first_ep(self):
        """
        First EP call
        """

        url = self._prepare_url('/first')
        self.log.info(url)
        response = requests.get(url)
        self.log.debug(response)
        return response.json()

    def second_ep(self):
        """
        Second EP call
        """
        url = self._prepare_url('/second')
        self.log.info(url)
        response = requests.get(url)
        self.log.debug(response)
        return response.json()

    def deafult_ep(self):
        """
        Default EP call
        """
        url = self._prepare_url('/')
        self.log.info(url)
        response = requests.get(url)
        self.log.debug(response)
        return response.json()

    def get_default_endpoint(self):
        """Get Default one"""
        url = self._prepare_url('/')
        self.log.info(url)
        response = requests.get(url)
        self.log.debug(response)
        return response.json()

    def get_all_data(self):
        """Get all data"""
        url = self._prepare_url('/pobierzAll')
        self.log.info(url)
        response = requests.get(url)
        self.log.debug(response)
        return response.json()


    def update_name(self):

        #new_put_data = {"FirstName": firstname, "LastName": lastname}
        url = self._prepare_url('/ZmienNazwisko2')
        self.log.info(url)
        response = requests.put(url,json={"FirstName":"Ewa", "LastName":"Pipka"})
        self.log.debug(response)
        return response.json()

if __name__ == '__main__':
    nc = NamesClient(url='http://127.0.0.1:8080')
    print nc.get_default_endpoint()
    print nc.add_person("Kaziu", "Kazimierski")
    print nc.get_all_data()
    print nc.first_ep()
    print nc.second_ep()
    print nc.deafult_ep()
    print nc.update_name()