#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <listobject.c>

static PyObject *
timsort(PyObject *self, PyObject *args)
{
    PyObject * arr;
    Py_ssize_t minrun;
    if (!PyArg_ParseTuple(args, "nO", &minrun, &arr))
        return NULL;
    PyList_Custom_Sort(arr, minrun);
    return PyLong_FromLong(1);
}

static PyMethodDef TimSortMethods[] = {
    {"timsort",  timsort, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef timsort_module = {
    PyModuleDef_HEAD_INIT,
    "timsort",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    TimSortMethods
};

PyMODINIT_FUNC
PyInit_customtimsort(void)
{
    return PyModule_Create(&timsort_module);
}

