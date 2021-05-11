class CustomRedirects_v5(object):
    """
    A class to query and use Pardot Custom Redirects.
    Custom redirects field reference: http://developer.pardot.com/kb/object-field-references#custom-redirect
    """

    def __init__(self, client):
        self.client = client
        self.fields = ['id','salesforceId','vanityUrl','trackedUrl','bitlyIsPersonalized', 'bitlyShortUrl','isDeleted','createdAt','updatedAt','createdById','updatedById','name','campaignId','destinationUrl','folderId','trackerDomainId','vanityUrlPath','gaMedium','gaSource','gaCampaign','gaContent','gaTerm']

    def query(self, fields=None, limit=1000, **kwargs):
        """
        Returns the custom redirects matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-4/custom-redirects/#supported-search-criteria
        """
        if fields is None:
            fields = self.fields
        
        response = self._get(path='', fields=fields, limit=limit, params=kwargs)

        # Ensure result['customRedirect'] is a list, no matter what.
        result = response.get('values')
        if result is None:
            return []
        elif isinstance(result, dict):
            return [result]
        else:
            return result

    def read(self, id=None, fields=None):
        """
        Returns the data for the custom redirect specified by <id>. <id> is the Pardot ID of the target custom redirect.
        """
        if fields is None:
            fields = self.fields
            
        response = self._get(path='/{id}'.format(id=id), fields=fields)
        return response

    def _get(self, object_name='custom-redirects', path=None, fields=None, limit=None, params=None):
        """GET requests for the Custom Redirect object."""
        if params is None:
            params = {}
        if fields is not None:
            params.update({"fields": ",".join(fields)})
        if limit is not None:
            params.update({"limit": limit})
        response = self.client.get(object_name=object_name, path=path, params=params, override_version=5)
        return response

    def _post(self, object_name='custom-redirects', path=None, params=None):
        """POST requests for the Custom Redirect object."""
        if params is None:
            params = {}
        response = self.client.post(object_name=object_name, path=path, params=params, override_version=5)
        return response
