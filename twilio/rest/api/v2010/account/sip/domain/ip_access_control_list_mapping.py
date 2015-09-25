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


class IpAccessControlListMappingList(ListResource):

    def __init__(self, version, account_sid, domain_sid):
        """
        Initialize the IpAccessControlListMappingList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param domain_sid: Contextual domain_sid
        
        :returns: IpAccessControlListMappingList
        :rtype: IpAccessControlListMappingList
        """
        super(IpAccessControlListMappingList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json'.format(**self._kwargs)

    def create(self, ip_access_control_list_sid):
        data = values.of({
            'IpAccessControlListSid': ip_access_control_list_sid,
        })
        
        return self._version.create(
            IpAccessControlListMappingInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            IpAccessControlListMappingInstance,
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
            IpAccessControlListMappingInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a IpAccessControlListMappingContext
        
        :param sid: Contextual sid
        
        :returns: IpAccessControlListMappingContext
        :rtype: IpAccessControlListMappingContext
        """
        return IpAccessControlListMappingContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAccessControlListMappingList>'


class IpAccessControlListMappingContext(InstanceContext):

    def __init__(self, version, account_sid, domain_sid, sid):
        """
        Initialize the IpAccessControlListMappingContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param domain_sid: Contextual domain_sid
        :param sid: Contextual sid
        
        :returns: IpAccessControlListMappingContext
        :rtype: IpAccessControlListMappingContext
        """
        super(IpAccessControlListMappingContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            IpAccessControlListMappingInstance,
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
        return '<Twilio.Api.V2010.IpAccessControlListMappingContext {}>'.format(context)


class IpAccessControlListMappingInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, domain_sid, sid=None):
        super(IpAccessControlListMappingInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = IpAccessControlListMappingContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['domain_sid'],
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
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

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
