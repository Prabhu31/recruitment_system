from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q, Count
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing candidate instances.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def create(self, request):
        """
        Create a new candidate.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(f"Validation errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Update an existing candidate.
        """
        partial = kwargs.pop('partial', False)
        candidate = self.get_object()
        serializer = self.get_serializer(candidate, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a candidate.
        """
        candidate = self.get_object()
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        """
        Search for candidates by name using query parameters.
        """
        query = request.query_params.get('q', '')
        if query:
            search_terms = query.split()
            filters = Q()
            for term in search_terms:
                filters |= Q(name__icontains=term)

            candidates = Candidate.objects.filter(filters).annotate(
                relevancy=Count('id', filter=Q(*[Q(name__icontains=term) for term in search_terms]))
            ).order_by('-relevancy')

            serializer = self.get_serializer(candidates, many=True)
            return Response(serializer.data)
        return Response([], status=status.HTTP_200_OK)