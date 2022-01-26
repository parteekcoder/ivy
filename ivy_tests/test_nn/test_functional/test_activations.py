"""
Collection of tests for unified neural network activation functions
"""

# global
import pytest
import numpy as np

# local
import ivy
import ivy.backends.numpy
import ivy_tests.helpers as helpers


# relu
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_relu(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.relu(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.relu, x), ivy.backends.numpy.relu(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.relu)


# leaky_relu
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_leaky_relu(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.leaky_relu(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.leaky_relu, x), ivy.backends.numpy.leaky_relu(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.leaky_relu)


# gelu
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "approx", [True, False])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_gelu(x, approx, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.gelu(x, approx)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.gelu, x, approx), ivy.backends.numpy.gelu(ivy.to_numpy(x), approx))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.gelu)


# tanh
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_tanh(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.tanh(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.tanh, x), ivy.backends.numpy.tanh(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.tanh)


# sigmoid
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_sigmoid(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.sigmoid(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.sigmoid, x), ivy.backends.numpy.sigmoid(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.sigmoid)


# softmax
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_softmax(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.softmax(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.softmax, x), ivy.backends.numpy.softmax(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.softmax)


# softplus
@pytest.mark.parametrize(
    "x", [[[-1., 1., 2.]]])
@pytest.mark.parametrize(
    "dtype", ['float32'])
@pytest.mark.parametrize(
    "tensor_fn", [ivy.array, helpers.var_fn])
def test_softplus(x, dtype, tensor_fn, dev_str, call):
    # smoke test
    x = tensor_fn(x, dtype, dev_str)
    ret = ivy.softplus(x)
    # type test
    assert ivy.is_array(ret)
    # cardinality test
    assert ret.shape == x.shape
    # value test
    assert np.allclose(call(ivy.softplus, x), ivy.backends.numpy.softplus(ivy.to_numpy(x)))
    # compilation test
    if not ivy.wrapped_mode():
        helpers.assert_compilable(ivy.softplus)
