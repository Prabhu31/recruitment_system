from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q, Count
from django.http import Http404
from .models import Candidate
from .serializers import CandidateSerializer
import logging

logger = logging.getLogger(__name__)

class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing candidate instances.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new candidate.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f"Candidate created with ID: {serializer.data.get('id')}")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Update an existing candidate.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        logger.info(f"Candidate updated with ID: {serializer.data.get('id')}")
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        Delete a candidate.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        logger.info(f"Candidate deleted with ID: {instance.id}")
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        """
        Search for candidates by name using query parameters.
        """
        query = request.query_params.get('q', '')
        if not query:
            return Response({'message': 'No search query provided.'}, status=status.HTTP_400_BAD_REQUEST)

        search_terms = query.split()
        filters = Q()
        for term in search_terms:
            filters |= Q(name__icontains=term)

        candidates = Candidate.objects.filter(filters).annotate(
            relevancy=Count('id', filter=Q(*[Q(name__icontains=term) for term in search_terms]))
        ).order_by('-relevancy')

        if candidates.exists():
            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data)
        return Response({'message': 'No candidates found.'}, status=status.HTTP_404_NOT_FOUND)