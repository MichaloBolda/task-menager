# Task Manager API

Backend REST API do zarządzania projektami i zadaniami zespołowymi.

## Problem
API umożliwia:
- tworzenie projektów
- dodawanie zadań do projektów
- przypisywanie zadań użytkownikom
- zmianę statusów zadań

## Zasoby
- User
- Project
- Task

## Relacje
- User 1 → N Project
- Project 1 → N Task
- User 1 → N Task (assigned)

## Technologie
- Python
- Django
- Django REST Framework
