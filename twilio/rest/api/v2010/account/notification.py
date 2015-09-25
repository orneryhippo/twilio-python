# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class NotificationList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the NotificationList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: NotificationList
        :rtype: NotificationList
        """
        super(NotificationList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Notifications'.format(**self._kwargs)

    def read(self, log=values.unset, message_date=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'Log': log,
            'MessageDate': serialize.iso8601_date(message_date),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, log=values.unset, message_date=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            'Log': log,
            'MessageDate': serialize.iso8601_date(message_date),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a NotificationContext
        
        :param sid: Contextual sid
        
        :returns: NotificationContext
        :rtype: NotificationContext
        """
        return NotificationContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationList>'


class NotificationContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the NotificationContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param sid: Contextual sid
        
        :returns: NotificationContext
        :rtype: NotificationContext
        """
        super(NotificationContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Notifications/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)


class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(NotificationInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'call_sid': payload['call_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'error_code': payload['error_code'],
            'log': payload['log'],
            'message_date': deserialize.rfc2822_datetime(payload['message_date']),
            'message_text': payload['message_text'],
            'more_info': payload['more_info'],
            'request_method': payload['request_method'],
            'request_url': payload['request_url'],
            'request_variables': payload['request_variables'],
            'response_body': payload['response_body'],
            'response_headers': payload['response_headers'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = NotificationContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """ The call_sid """
        return self._properties['call_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def error_code(self):
        """ The error_code """
        return self._properties['error_code']

    @property
    def log(self):
        """ The log """
        return self._properties['log']

    @property
    def message_date(self):
        """ The message_date """
        return self._properties['message_date']

    @property
    def message_text(self):
        """ The message_text """
        return self._properties['message_text']

    @property
    def more_info(self):
        """ The more_info """
        return self._properties['more_info']

    @property
    def request_method(self):
        """ The request_method """
        return self._properties['request_method']

    @property
    def request_url(self):
        """ The request_url """
        return self._properties['request_url']

    @property
    def request_variables(self):
        """ The request_variables """
        return self._properties['request_variables']

    @property
    def response_body(self):
        """ The response_body """
        return self._properties['response_body']

    @property
    def response_headers(self):
        """ The response_headers """
        return self._properties['response_headers']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
