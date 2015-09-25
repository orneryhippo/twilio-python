# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.conversations.v1.conversation.participant import ParticipantList


class InProgressList(ListResource):

    def __init__(self, version):
        """
        Initialize the InProgressList
        
        :param Version version: Version that contains the resource
        
        :returns: InProgressList
        :rtype: InProgressList
        """
        super(InProgressList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Conversations/InProgress'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            InProgressInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            InProgressInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a InProgressContext
        
        :param sid: Contextual sid
        
        :returns: InProgressContext
        :rtype: InProgressContext
        """
        return InProgressContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.InProgressList>'


class InProgressContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the InProgressContext
        
        :param Version version
        :param sid: Contextual sid
        
        :returns: InProgressContext
        :rtype: InProgressContext
        """
        super(InProgressContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Conversations/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._participants = None

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                conversation_sid=self._kwargs['sid'],
            )
        return self._participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.InProgressContext {}>'.format(context)


class InProgressInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        super(InProgressInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'status': payload['status'],
            'duration': payload['duration'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = InProgressContext(
                self._version,
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def duration(self):
        """ The duration """
        return self._properties['duration']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def start_time(self):
        """ The start_time """
        return self._properties['start_time']

    @property
    def end_time(self):
        """ The end_time """
        return self._properties['end_time']

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    @property
    def participants(self):
        return self._context.participants
