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
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics import StatisticsContext
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queues_statistics import StatisticsList


class TaskQueueList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the TaskQueueList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: Contextual workspace_sid
        
        :returns: TaskQueueList
        :rtype: TaskQueueList
        """
        super(TaskQueueList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues'.format(**self._kwargs)
        
        # Components
        self._statistics = None

    def read(self, friendly_name=values.unset,
             evaluate_worker_attributes=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'FriendlyName': friendly_name,
            'EvaluateWorkerAttributes': evaluate_worker_attributes,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TaskQueueInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset,
             evaluate_worker_attributes=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            'FriendlyName': friendly_name,
            'EvaluateWorkerAttributes': evaluate_worker_attributes,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            TaskQueueInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, reservation_activity_sid,
               assignment_activity_sid, target_workers=values.unset,
               max_reserved_workers=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'ReservationActivitySid': reservation_activity_sid,
            'AssignmentActivitySid': assignment_activity_sid,
            'TargetWorkers': target_workers,
            'MaxReservedWorkers': max_reserved_workers,
        })
        
        return self._version.create(
            TaskQueueInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: StatisticsList
        :rtype: StatisticsList
        """
        if self._statistics is None:
            self._statistics = StatisticsList(self._version, **self._kwargs)
        return self._statistics

    def __call__(self, sid):
        """
        Constructs a TaskQueueContext
        
        :param sid: Contextual sid
        
        :returns: TaskQueueContext
        :rtype: TaskQueueContext
        """
        return TaskQueueContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueList>'


class TaskQueueContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the TaskQueueContext
        
        :param Version version
        :param sid: Contextual sid
        :param workspace_sid: Contextual workspace_sid
        
        :returns: TaskQueueContext
        :rtype: TaskQueueContext
        """
        super(TaskQueueContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TaskQueueInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset, target_workers=values.unset,
               reservation_activity_sid=values.unset,
               assignment_activity_sid=values.unset,
               max_reserved_workers=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'TargetWorkers': target_workers,
            'ReservationActivitySid': reservation_activity_sid,
            'AssignmentActivitySid': assignment_activity_sid,
            'MaxReservedWorkers': max_reserved_workers,
        })
        
        return self._version.update(
            TaskQueueInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._version,
                workspace_sid=self._kwargs['workspace_sid'],
                task_queue_sid=self._kwargs['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.TaskQueueContext {}>'.format(context)


class TaskQueueInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        super(TaskQueueInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'assignment_activity_sid': payload['assignment_activity_sid'],
            'assignment_activity_name': payload['assignment_activity_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'max_reserved_workers': payload['max_reserved_workers'],
            'reservation_activity_sid': payload['reservation_activity_sid'],
            'reservation_activity_name': payload['reservation_activity_name'],
            'sid': payload['sid'],
            'target_workers': payload['target_workers'],
            'url': payload['url'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TaskQueueContext(
                self._version,
                self._context_properties['workspace_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def assignment_activity_sid(self):
        """ The assignment_activity_sid """
        return self._properties['assignment_activity_sid']

    @property
    def assignment_activity_name(self):
        """ The assignment_activity_name """
        return self._properties['assignment_activity_name']

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
    def max_reserved_workers(self):
        """ The max_reserved_workers """
        return self._properties['max_reserved_workers']

    @property
    def reservation_activity_sid(self):
        """ The reservation_activity_sid """
        return self._properties['reservation_activity_sid']

    @property
    def reservation_activity_name(self):
        """ The reservation_activity_name """
        return self._properties['reservation_activity_name']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def target_workers(self):
        """ The target_workers """
        return self._properties['target_workers']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._properties['workspace_sid']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, target_workers=values.unset,
               reservation_activity_sid=values.unset,
               assignment_activity_sid=values.unset,
               max_reserved_workers=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            target_workers=target_workers,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            max_reserved_workers=max_reserved_workers,
        )

    def delete(self):
        self._context.delete()

    @property
    def statistics(self):
        return self._context.statistics
