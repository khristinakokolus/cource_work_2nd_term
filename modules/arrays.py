"""
Module that represents the needed data structures for the investigation.
That is mostly based on the materials from the labs.
Also using the book Data Structures and
Algorithms Using Python – R. Necaise.
"""
import ctypes


class Array:
    """Creates an array with size elements"""
    def __init__(self, size):
        """(Array, int)

        Creates the array structure using the
        ctypes module.
        """
        self._size = size
        self._elements = (ctypes.py_object * size)()
        self.clear(None)

    def __len__(self):
        """(Array) -> int

        Returns the size of the array.
        """
        return self._size

    def __getitem__(self, index):
        """(Array, int) -> str

        Gets the content of the index element.
        """
        assert 0 <= index < len(self),\
            "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """(Array, int, str)

        Puts the value in the array element at index position.
        """
        assert 0 <= index < len(self),\
            "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """(Array, str)

        Clears the array by setting each element
        to the given value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """(Array)

        Returns the array's iterator for traversing
        the elements.
        """
        return _ArrayIterator(self._elements)

    def __str__(self):
        """(Array)
        Returns the printable representation of array.
        """
        str_array = "["
        for i in range(self._size):
           str_array += str(self[i]) + ", "
        str_array = str_array[:-2] + "]"
        return str_array


class _ArrayIterator:
    """An iterator for the Array ADT."""
    def __init__(self, the_array):
        """(_ArrayIterator)

        Represents the iterator.
        """
        self._array = the_array
        self._cur_index = 0

    def __iter__(self):
        """(_ArrayIterator)

        The iterator.
        """
        return self

    def __next__(self):
        """(_ArrayIterator)

        The next value of iteration.
        """
        if self._cur_index < len(self._array):
            entry = self._array[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        """(DynamicArray)

        Creates an empty array.
        """
        self._num_elements = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):
        """(DynamicArray)

        Returns number of elements stored in the array.
        """
        return self._num_elements

    def __getitem__(self, index):
        """(DynamicArray, int)

        Returns element at index.
        """
        if not 0 <= index < self._num_elements:
            raise IndexError('invalid index')
        return self._array[index]

    def append(self, item):
        """(DynamicArray, str)

        Add object to end of the array.
        """
        if self._num_elements == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._num_elements] = item
        self._num_elements += 1

    def _resize(self, capacity):
        """(DynamicArray, int)

        Resizes internal array to the certain capacity.
        """
        bigger_array = self._make_array(capacity)
        for i in range(self._num_elements):
            bigger_array[i] = self._array[i]
        self._array = bigger_array
        self._capacity = capacity

    def _make_array(self, capacity):
        """(DynamicArray, int) -> Array

        Return new array with capacity.
        """
        return (capacity * ctypes.py_object)()

    def remove(self, value):
        """(DynamicArray, str)

        Remove the first occurrence of value.
        If thee is no such value raises ValueError.
        """
        for i in range(self._num_elements):
            if self._array[i] == value:
                for j in range(i, self._num_elements - 1):
                    self._array[j] = self._array[j + 1]
                self._array[self._num_elements - 1] = None
                self._num_elements -= 1

                return
        raise ValueError("value not found")

    def __str__(self):
        """(DynamicArray) -> str
        Returns printable representation of DynamicArray.
        """
        str_dynamic_array = "["
        for i in range(self._num_elements):
           str_dynamic_array += str(self[i]) + ", "
        str_dynamic_array = str_dynamic_array[:-2] + "]"
        return str_dynamic_array
