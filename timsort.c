#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <listobject.c>

static PyObject *
Get_minrun(PyObject *self, PyObject *args)
{
    Py_ssize_t size_of_array;
    PyObject * buffer;
    if (!PyArg_ParseTuple(args, "On", &buffer, &size_of_array))
        return NULL;

    const char* path = PyBytes_AS_STRING(PyUnicode_AsEncodedString(PyObject_Repr(buffer), "utf-8", "~E~"));
    //char line[30] = {0};
    //int line_count = -3;
    printf(path);
    FILE *file = fopen(path, "r");
    fclose(file);

    /*int first_size = 0, step = 1;
    int minrun = 2;
    while (fgets(line, 30, file))
    {
        if (line_count == -3) {
            first_size = atoi(line);
        } else if (line_count == -2) {
            step = atoi(line);
        } else if (line_count >= 0 && first_size + line_count * step == size_of_array) {
            minrun = atoi(line);
        }
        line_count++;
    }
    fclose(file);*/
    //return PyLong_FromLong(minrun);
    return PyLong_FromLong(1);
}

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
    {"Get_minrun",  Get_minrun, METH_VARARGS,
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

