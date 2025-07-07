from collections.abc import Sequence
from typing import TypeAlias, Union, overload

import drjit


from builtins import (
    bool as Bool,
    float as Float,
    float as Float16,
    float as Float32,
    float as Float64,
    int as Int,
    int as Int16,
    int as Int32,
    int as Int64,
    int as UInt,
    int as UInt16,
    int as UInt32,
    int as UInt64
)

class Array0b(drjit.ArrayBase[Array0b, _Array0bCp, bool, bool, bool, Array0b, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0f(drjit.ArrayBase[Array0f, _Array0fCp, float, float, float, Array0f, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0f16(drjit.ArrayBase[Array0f16, _Array0f16Cp, float, float, float, Array0f16, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0f64(drjit.ArrayBase[Array0f64, _Array0f64Cp, float, float, float, Array0f64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0i(drjit.ArrayBase[Array0i, _Array0iCp, int, int, int, Array0i, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0i64(drjit.ArrayBase[Array0i64, _Array0i64Cp, int, int, int, Array0i64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0u(drjit.ArrayBase[Array0u, _Array0uCp, int, int, int, Array0u, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array0u64(drjit.ArrayBase[Array0u64, _Array0u64Cp, int, int, int, Array0u64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1b(drjit.ArrayBase[Array1b, _Array1bCp, bool, bool, bool, Array1b, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1f(drjit.ArrayBase[Array1f, _Array1fCp, float, float, float, Array1f, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1f16(drjit.ArrayBase[Array1f16, _Array1f16Cp, float, float, float, Array1f16, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1f64(drjit.ArrayBase[Array1f64, _Array1f64Cp, float, float, float, Array1f64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1i(drjit.ArrayBase[Array1i, _Array1iCp, int, int, int, Array1i, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1i64(drjit.ArrayBase[Array1i64, _Array1i64Cp, int, int, int, Array1i64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1u(drjit.ArrayBase[Array1u, _Array1uCp, int, int, int, Array1u, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array1u64(drjit.ArrayBase[Array1u64, _Array1u64Cp, int, int, int, Array1u64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array22b(drjit.ArrayBase[Array22b, _Array22bCp, Array2b, _Array2bCp, Array2b, Array22b, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array22f(drjit.ArrayBase[Array22f, _Array22fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array22f16(drjit.ArrayBase[Array22f16, _Array22f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array22f64(drjit.ArrayBase[Array22f64, _Array22f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2b(drjit.ArrayBase[Array2b, _Array2bCp, bool, bool, bool, Array2b, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2f(drjit.ArrayBase[Array2f, _Array2fCp, float, float, float, Array2f, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2f16(drjit.ArrayBase[Array2f16, _Array2f16Cp, float, float, float, Array2f16, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2f64(drjit.ArrayBase[Array2f64, _Array2f64Cp, float, float, float, Array2f64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2i(drjit.ArrayBase[Array2i, _Array2iCp, int, int, int, Array2i, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2i64(drjit.ArrayBase[Array2i64, _Array2i64Cp, int, int, int, Array2i64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2u(drjit.ArrayBase[Array2u, _Array2uCp, int, int, int, Array2u, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array2u64(drjit.ArrayBase[Array2u64, _Array2u64Cp, int, int, int, Array2u64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array334b(drjit.ArrayBase[Array334b, _Array334bCp, Array34b, _Array34bCp, Array34b, Array334b, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array334f(drjit.ArrayBase[Array334f, _Array334fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array334f16(drjit.ArrayBase[Array334f16, _Array334f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array334f64(drjit.ArrayBase[Array334f64, _Array334f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array33b(drjit.ArrayBase[Array33b, _Array33bCp, Array3b, _Array3bCp, Array3b, Array33b, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array33f(drjit.ArrayBase[Array33f, _Array33fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array33f16(drjit.ArrayBase[Array33f16, _Array33f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array33f64(drjit.ArrayBase[Array33f64, _Array33f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array34b(drjit.ArrayBase[Array34b, _Array34bCp, Array4b, _Array4bCp, Array4b, Array34b, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array34f(drjit.ArrayBase[Array34f, _Array34fCp, Array4f, _Array4fCp, Array4f, Array34f, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array34f16(drjit.ArrayBase[Array34f16, _Array34f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array34f16, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array34f64(drjit.ArrayBase[Array34f64, _Array34f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array34f64, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3b(drjit.ArrayBase[Array3b, _Array3bCp, bool, bool, bool, Array3b, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3f(drjit.ArrayBase[Array3f, _Array3fCp, float, float, float, Array3f, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3f16(drjit.ArrayBase[Array3f16, _Array3f16Cp, float, float, float, Array3f16, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3f64(drjit.ArrayBase[Array3f64, _Array3f64Cp, float, float, float, Array3f64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3i(drjit.ArrayBase[Array3i, _Array3iCp, int, int, int, Array3i, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3i64(drjit.ArrayBase[Array3i64, _Array3i64Cp, int, int, int, Array3i64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3u(drjit.ArrayBase[Array3u, _Array3uCp, int, int, int, Array3u, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array3u64(drjit.ArrayBase[Array3u64, _Array3u64Cp, int, int, int, Array3u64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array41b(drjit.ArrayBase[Array41b, _Array41bCp, Array1b, _Array1bCp, Array1b, Array41b, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array41f(drjit.ArrayBase[Array41f, _Array41fCp, Array1f, _Array1fCp, Array1f, Array41f, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array41f16(drjit.ArrayBase[Array41f16, _Array41f16Cp, Array1f16, _Array1f16Cp, Array1f16, Array41f16, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array41f64(drjit.ArrayBase[Array41f64, _Array41f64Cp, Array1f64, _Array1f64Cp, Array1f64, Array41f64, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array43b(drjit.ArrayBase[Array43b, _Array43bCp, Array3b, _Array3bCp, Array3b, Array43b, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array43f(drjit.ArrayBase[Array43f, _Array43fCp, Array3f, _Array3fCp, Array3f, Array43f, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array43f16(drjit.ArrayBase[Array43f16, _Array43f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array43f16, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array43f64(drjit.ArrayBase[Array43f64, _Array43f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array43f64, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array441b(drjit.ArrayBase[Array441b, _Array441bCp, Array41b, _Array41bCp, Array41b, Array441b, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array441f(drjit.ArrayBase[Array441f, _Array441fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array441f16(drjit.ArrayBase[Array441f16, _Array441f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array441f64(drjit.ArrayBase[Array441f64, _Array441f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array443b(drjit.ArrayBase[Array443b, _Array443bCp, Array43b, _Array43bCp, Array43b, Array443b, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array443f(drjit.ArrayBase[Array443f, _Array443fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array443f16(drjit.ArrayBase[Array443f16, _Array443f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array443f64(drjit.ArrayBase[Array443f64, _Array443f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array444b(drjit.ArrayBase[Array444b, _Array444bCp, Array44b, _Array44bCp, Array44b, Array444b, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array444f(drjit.ArrayBase[Array444f, _Array444fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array444f16(drjit.ArrayBase[Array444f16, _Array444f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array444f64(drjit.ArrayBase[Array444f64, _Array444f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array44b(drjit.ArrayBase[Array44b, _Array44bCp, Array4b, _Array4bCp, Array4b, Array44b, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array44f(drjit.ArrayBase[Array44f, _Array44fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array44f16(drjit.ArrayBase[Array44f16, _Array44f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array44f64(drjit.ArrayBase[Array44f64, _Array44f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4b(drjit.ArrayBase[Array4b, _Array4bCp, bool, bool, bool, Array4b, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4f(drjit.ArrayBase[Array4f, _Array4fCp, float, float, float, Array4f, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4f16(drjit.ArrayBase[Array4f16, _Array4f16Cp, float, float, float, Array4f16, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4f64(drjit.ArrayBase[Array4f64, _Array4f64Cp, float, float, float, Array4f64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4i(drjit.ArrayBase[Array4i, _Array4iCp, int, int, int, Array4i, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4i64(drjit.ArrayBase[Array4i64, _Array4i64Cp, int, int, int, Array4i64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4u(drjit.ArrayBase[Array4u, _Array4uCp, int, int, int, Array4u, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Array4u64(drjit.ArrayBase[Array4u64, _Array4u64Cp, int, int, int, Array4u64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXb(drjit.ArrayBase[ArrayXb, _ArrayXbCp, bool, bool, bool, ArrayXb, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXf(drjit.ArrayBase[ArrayXf, _ArrayXfCp, float, float, float, ArrayXf, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXf16(drjit.ArrayBase[ArrayXf16, _ArrayXf16Cp, float, float, float, ArrayXf16, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXf64(drjit.ArrayBase[ArrayXf64, _ArrayXf64Cp, float, float, float, ArrayXf64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXi(drjit.ArrayBase[ArrayXi, _ArrayXiCp, int, int, int, ArrayXi, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXi64(drjit.ArrayBase[ArrayXi64, _ArrayXi64Cp, int, int, int, ArrayXi64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXu(drjit.ArrayBase[ArrayXu, _ArrayXuCp, int, int, int, ArrayXu, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class ArrayXu64(drjit.ArrayBase[ArrayXu64, _ArrayXu64Cp, int, int, int, ArrayXu64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Complex2f(drjit.ArrayBase[Complex2f, _Complex2fCp, float, float, float, Array2f, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Complex2f64(drjit.ArrayBase[Complex2f64, _Complex2f64Cp, float, float, float, Array2f64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix2f(drjit.ArrayBase[Matrix2f, _Matrix2fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix2f16(drjit.ArrayBase[Matrix2f16, _Matrix2f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix2f64(drjit.ArrayBase[Matrix2f64, _Matrix2f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix34f(drjit.ArrayBase[Matrix34f, _Matrix34fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix34f16(drjit.ArrayBase[Matrix34f16, _Matrix34f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix34f64(drjit.ArrayBase[Matrix34f64, _Matrix34f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix3f(drjit.ArrayBase[Matrix3f, _Matrix3fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix3f16(drjit.ArrayBase[Matrix3f16, _Matrix3f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix3f64(drjit.ArrayBase[Matrix3f64, _Matrix3f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix41f(drjit.ArrayBase[Matrix41f, _Matrix41fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix41f16(drjit.ArrayBase[Matrix41f16, _Matrix41f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix41f64(drjit.ArrayBase[Matrix41f64, _Matrix41f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix43f(drjit.ArrayBase[Matrix43f, _Matrix43fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix43f16(drjit.ArrayBase[Matrix43f16, _Matrix43f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix43f64(drjit.ArrayBase[Matrix43f64, _Matrix43f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix44f(drjit.ArrayBase[Matrix44f, _Matrix44fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix44f16(drjit.ArrayBase[Matrix44f16, _Matrix44f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix44f64(drjit.ArrayBase[Matrix44f64, _Matrix44f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix4f(drjit.ArrayBase[Matrix4f, _Matrix4fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix4f16(drjit.ArrayBase[Matrix4f16, _Matrix4f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Matrix4f64(drjit.ArrayBase[Matrix4f64, _Matrix4f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class PCG32:
    """
    Implementation of PCG32, a member of the PCG family of random number generators
    proposed by Melissa O'Neill.

    PCG combines a Linear Congruential Generator (LCG) with a permutation function
    that yields high-quality pseudorandom variates while at the same time requiring
    very low computational cost and internal state (only 128 bit in the case of
    PCG32).

    More detail on the PCG family of pseudorandom number generators can be found
    `here <https://www.pcg-random.org/index.html>`__.

    The :py:class:`PCG32` class is implemented as a :ref:`PyTree <pytrees>`, which
    means that it is compatible with symbolic function calls, loops, etc.
    """

    @overload
    def __init__(self, size: int = 1, initstate: int = UInt64(0x853c49e6748fea9b), initseq: int = UInt64(0xda3e39cb94b95bdb)) -> None:
        """
        Initialize a random number generator that generates ``size`` variates in parallel.

        The ``initstate`` and ``initseq`` inputs determine the initial state and increment
        of the linear congruential generator. Their defaults values are based on the
        original implementation.

        The implementation of this routine internally calls py:func:`seed`, with one
        small twist. When multiple random numbers are being generated in parallel, the
        constructor adds an offset equal to :py:func:`drjit.arange(UInt64, size)
        <drjit.arange>` to both ``initstate`` and ``initseq`` to de-correlate the
        generated sequences.
        """

    @overload
    def __init__(self, arg: PCG32) -> None:
        """Copy-construct a new PCG32 instance from an existing instance."""

    def seed(self, initstate: int = UInt64(0x853c49e6748fea9b), initseq: int = UInt64(0xda3e39cb94b95bdb)) -> None:
        """
        Seed the random number generator with the given initial state and sequence ID.

        The ``initstate`` and ``initseq`` inputs determine the initial state and increment
        of the linear congruential generator. Their values are the defaults from the
        original implementation.
        """

    @overload
    def next_uint32(self) -> int:
        """
        Generate a uniformly distributed unsigned 32-bit random number

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint32(self, arg: bool, /) -> int: ...

    def next_uint32_bounded(self, bound: int, mask: bool = Bool(True)) -> int:
        r"""
        Generate a uniformly distributed 32-bit integer number on the
        interval :math:`[0, \texttt{bound})`.

        To ensure an unbiased result, the implementation relies on an iterative
        scheme that typically finishes after 1-2 iterations.
        """

    @overload
    def next_uint64(self) -> int:
        """
        Generate a uniformly distributed unsigned 64-bit random number

        Internally, the function calls :py:func:`next_uint32` twice.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint64(self, arg: bool, /) -> int: ...

    def next_uint64_bounded(self, bound: int, mask: bool = Bool(True)) -> int:
        r"""
        Generate a uniformly distributed 64-bit integer number on the
        interval :math:`[0, \texttt{bound})`.

        To ensure an unbiased result, the implementation relies on an iterative
        scheme that typically finishes after 1-2 iterations.
        """

    @overload
    def next_float32(self) -> float: ...

    @overload
    def next_float32(self, arg: bool, /) -> float:
        """
        Generate a uniformly distributed single precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float64(self) -> float: ...

    @overload
    def next_float64(self, arg: bool, /) -> float:
        """
        Generate a uniformly distributed double precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    def __add__(self, arg: int, /) -> PCG32:
        """
        Advance the pseudorandom number generator.

        This function implements a multi-step advance function that is equivalent to
        (but more efficient than) calling the random number generator ``arg`` times
        in sequence.

        This is useful to advance a newly constructed PRNG to a certain known state.
        """

    def __iadd__(self, arg: int, /) -> PCG32:
        """In-place addition operator based on :py:func:`__add__`."""

    @overload
    def __sub__(self, arg: int, /) -> PCG32:
        """
        Rewind the pseudorandom number generator.

        This function implements the opposite of ``__add__`` to step a PRNG backwards.
        It can also compute the *difference* (as counted by the number of internal
        ``next_uint32`` steps) between two :py:class:`PCG32` instances. This assumes
        that the two instances were consistently seeded.
        """

    @overload
    def __sub__(self, arg: PCG32, /) -> int: ...

    def __isub__(self, arg: Int64, /) -> PCG32: # type: ignore
        """In-place subtraction operator based on :py:func:`__sub__`."""

    @property
    def state(self) -> int:
        """
        Sequence state of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @state.setter
    def state(self, arg: int, /) -> None: ...

    @property
    def inc(self) -> int:
        """
        Sequence increment of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @inc.setter
    def inc(self, arg: int, /) -> None: ...

    DRJIT_STRUCT: dict = {'state' : int, 'inc' : int}

class Quaternion4f(drjit.ArrayBase[Quaternion4f, _Quaternion4fCp, float, float, float, Array4f, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Quaternion4f16(drjit.ArrayBase[Quaternion4f16, _Quaternion4f16Cp, float, float, float, Array4f16, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Quaternion4f64(drjit.ArrayBase[Quaternion4f64, _Quaternion4f64Cp, float, float, float, Array4f64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXb(drjit.ArrayBase[TensorXb, _TensorXbCp, TensorXb, _TensorXbCp, TensorXb, ArrayXb, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXf(drjit.ArrayBase[TensorXf, _TensorXfCp, TensorXf, _TensorXfCp, TensorXf, ArrayXf, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXf16(drjit.ArrayBase[TensorXf16, _TensorXf16Cp, TensorXf16, _TensorXf16Cp, TensorXf16, ArrayXf16, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXf64(drjit.ArrayBase[TensorXf64, _TensorXf64Cp, TensorXf64, _TensorXf64Cp, TensorXf64, ArrayXf64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXi(drjit.ArrayBase[TensorXi, _TensorXiCp, TensorXi, _TensorXiCp, TensorXi, ArrayXi, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXi64(drjit.ArrayBase[TensorXi64, _TensorXi64Cp, TensorXi64, _TensorXi64Cp, TensorXi64, ArrayXi64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXu(drjit.ArrayBase[TensorXu, _TensorXuCp, TensorXu, _TensorXuCp, TensorXu, ArrayXu, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class TensorXu64(drjit.ArrayBase[TensorXu64, _TensorXu64Cp, TensorXu64, _TensorXu64Cp, TensorXu64, ArrayXu64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class Texture1f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture1f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture1f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

_Array0bCp: TypeAlias = Union['Array0b', bool]

_Array0f16Cp: TypeAlias = Union['Array0f16', float, '_Array0u64Cp']

_Array0f64Cp: TypeAlias = Union['Array0f64', float, '_Array0fCp']

_Array0fCp: TypeAlias = Union['Array0f', float, '_Array0f16Cp']

_Array0i64Cp: TypeAlias = Union['Array0i64', int, '_Array0uCp']

_Array0iCp: TypeAlias = Union['Array0i', int, '_Array0bCp']

_Array0u64Cp: TypeAlias = Union['Array0u64', int, '_Array0i64Cp']

_Array0uCp: TypeAlias = Union['Array0u', int, '_Array0iCp']

_Array1bCp: TypeAlias = Union['Array1b', bool]

_Array1f16Cp: TypeAlias = Union['Array1f16', float, '_Array1u64Cp']

_Array1f64Cp: TypeAlias = Union['Array1f64', float, '_Array1fCp']

_Array1fCp: TypeAlias = Union['Array1f', float, '_Array1f16Cp']

_Array1i64Cp: TypeAlias = Union['Array1i64', int, '_Array1uCp']

_Array1iCp: TypeAlias = Union['Array1i', int, '_Array1bCp']

_Array1u64Cp: TypeAlias = Union['Array1u64', int, '_Array1i64Cp']

_Array1uCp: TypeAlias = Union['Array1u', int, '_Array1iCp']

_Array22bCp: TypeAlias = Union['Array22b', '_Array2bCp']

_Array22f16Cp: TypeAlias = Union['Array22f16', '_Array2f16Cp']

_Array22f64Cp: TypeAlias = Union['Array22f64', '_Array2f64Cp', '_Array22fCp']

_Array22fCp: TypeAlias = Union['Array22f', '_Array2fCp', '_Array22f16Cp']

_Array2bCp: TypeAlias = Union['Array2b', bool]

_Array2f16Cp: TypeAlias = Union['Array2f16', float, '_Array2u64Cp']

_Array2f64Cp: TypeAlias = Union['Array2f64', float, '_Array2fCp']

_Array2fCp: TypeAlias = Union['Array2f', float, '_Array2f16Cp']

_Array2i64Cp: TypeAlias = Union['Array2i64', int, '_Array2uCp']

_Array2iCp: TypeAlias = Union['Array2i', int, '_Array2bCp']

_Array2u64Cp: TypeAlias = Union['Array2u64', int, '_Array2i64Cp']

_Array2uCp: TypeAlias = Union['Array2u', int, '_Array2iCp']

_Array334bCp: TypeAlias = Union['Array334b', '_Array34bCp']

_Array334f16Cp: TypeAlias = Union['Array334f16', '_Array34f16Cp']

_Array334f64Cp: TypeAlias = Union['Array334f64', '_Array34f64Cp', '_Array334fCp']

_Array334fCp: TypeAlias = Union['Array334f', '_Array34fCp', '_Array334f16Cp']

_Array33bCp: TypeAlias = Union['Array33b', '_Array3bCp']

_Array33f16Cp: TypeAlias = Union['Array33f16', '_Array3f16Cp']

_Array33f64Cp: TypeAlias = Union['Array33f64', '_Array3f64Cp', '_Array33fCp']

_Array33fCp: TypeAlias = Union['Array33f', '_Array3fCp', '_Array33f16Cp']

_Array34bCp: TypeAlias = Union['Array34b', '_Array4bCp']

_Array34f16Cp: TypeAlias = Union['Array34f16', '_Array4f16Cp']

_Array34f64Cp: TypeAlias = Union['Array34f64', '_Array4f64Cp', '_Array34fCp']

_Array34fCp: TypeAlias = Union['Array34f', '_Array4fCp', '_Array34f16Cp']

_Array3bCp: TypeAlias = Union['Array3b', bool]

_Array3f16Cp: TypeAlias = Union['Array3f16', float, '_Array3u64Cp']

_Array3f64Cp: TypeAlias = Union['Array3f64', float, '_Array3fCp']

_Array3fCp: TypeAlias = Union['Array3f', float, '_Array3f16Cp']

_Array3i64Cp: TypeAlias = Union['Array3i64', int, '_Array3uCp']

_Array3iCp: TypeAlias = Union['Array3i', int, '_Array3bCp']

_Array3u64Cp: TypeAlias = Union['Array3u64', int, '_Array3i64Cp']

_Array3uCp: TypeAlias = Union['Array3u', int, '_Array3iCp']

_Array41bCp: TypeAlias = Union['Array41b', '_Array1bCp']

_Array41f16Cp: TypeAlias = Union['Array41f16', '_Array1f16Cp']

_Array41f64Cp: TypeAlias = Union['Array41f64', '_Array1f64Cp', '_Array41fCp']

_Array41fCp: TypeAlias = Union['Array41f', '_Array1fCp', '_Array41f16Cp']

_Array43bCp: TypeAlias = Union['Array43b', '_Array3bCp']

_Array43f16Cp: TypeAlias = Union['Array43f16', '_Array3f16Cp']

_Array43f64Cp: TypeAlias = Union['Array43f64', '_Array3f64Cp', '_Array43fCp']

_Array43fCp: TypeAlias = Union['Array43f', '_Array3fCp', '_Array43f16Cp']

_Array441bCp: TypeAlias = Union['Array441b', '_Array41bCp']

_Array441f16Cp: TypeAlias = Union['Array441f16', '_Array41f16Cp']

_Array441f64Cp: TypeAlias = Union['Array441f64', '_Array41f64Cp', '_Array441fCp']

_Array441fCp: TypeAlias = Union['Array441f', '_Array41fCp', '_Array441f16Cp']

_Array443bCp: TypeAlias = Union['Array443b', '_Array43bCp']

_Array443f16Cp: TypeAlias = Union['Array443f16', '_Array43f16Cp']

_Array443f64Cp: TypeAlias = Union['Array443f64', '_Array43f64Cp', '_Array443fCp']

_Array443fCp: TypeAlias = Union['Array443f', '_Array43fCp', '_Array443f16Cp']

_Array444bCp: TypeAlias = Union['Array444b', '_Array44bCp']

_Array444f16Cp: TypeAlias = Union['Array444f16', '_Array44f16Cp']

_Array444f64Cp: TypeAlias = Union['Array444f64', '_Array44f64Cp', '_Array444fCp']

_Array444fCp: TypeAlias = Union['Array444f', '_Array44fCp', '_Array444f16Cp']

_Array44bCp: TypeAlias = Union['Array44b', '_Array4bCp']

_Array44f16Cp: TypeAlias = Union['Array44f16', '_Array4f16Cp']

_Array44f64Cp: TypeAlias = Union['Array44f64', '_Array4f64Cp', '_Array44fCp']

_Array44fCp: TypeAlias = Union['Array44f', '_Array4fCp', '_Array44f16Cp']

_Array4bCp: TypeAlias = Union['Array4b', bool]

_Array4f16Cp: TypeAlias = Union['Array4f16', float, '_Array4u64Cp']

_Array4f64Cp: TypeAlias = Union['Array4f64', float, '_Array4fCp']

_Array4fCp: TypeAlias = Union['Array4f', float, '_Array4f16Cp']

_Array4i64Cp: TypeAlias = Union['Array4i64', int, '_Array4uCp']

_Array4iCp: TypeAlias = Union['Array4i', int, '_Array4bCp']

_Array4u64Cp: TypeAlias = Union['Array4u64', int, '_Array4i64Cp']

_Array4uCp: TypeAlias = Union['Array4u', int, '_Array4iCp']

_ArrayXbCp: TypeAlias = Union['ArrayXb', bool]

_ArrayXf16Cp: TypeAlias = Union['ArrayXf16', float, '_ArrayXu64Cp']

_ArrayXf64Cp: TypeAlias = Union['ArrayXf64', float, '_ArrayXfCp']

_ArrayXfCp: TypeAlias = Union['ArrayXf', float, '_ArrayXf16Cp']

_ArrayXi64Cp: TypeAlias = Union['ArrayXi64', int, '_ArrayXuCp']

_ArrayXiCp: TypeAlias = Union['ArrayXi', int, '_ArrayXbCp']

_ArrayXu64Cp: TypeAlias = Union['ArrayXu64', int, '_ArrayXi64Cp']

_ArrayXuCp: TypeAlias = Union['ArrayXu', int, '_ArrayXiCp']

_Complex2f64Cp: TypeAlias = Union['Complex2f64', float, '_Complex2fCp']

_Complex2fCp: TypeAlias = Union['Complex2f', float]

_Matrix2f16Cp: TypeAlias = Union['Matrix2f16', '_Array2f16Cp']

_Matrix2f64Cp: TypeAlias = Union['Matrix2f64', '_Array2f64Cp', '_Matrix2fCp']

_Matrix2fCp: TypeAlias = Union['Matrix2f', '_Array2fCp', '_Matrix2f16Cp']

_Matrix34f16Cp: TypeAlias = Union['Matrix34f16', '_Array34f16Cp']

_Matrix34f64Cp: TypeAlias = Union['Matrix34f64', '_Array34f64Cp', '_Matrix34fCp']

_Matrix34fCp: TypeAlias = Union['Matrix34f', '_Array34fCp', '_Matrix34f16Cp']

_Matrix3f16Cp: TypeAlias = Union['Matrix3f16', '_Array3f16Cp']

_Matrix3f64Cp: TypeAlias = Union['Matrix3f64', '_Array3f64Cp', '_Matrix3fCp']

_Matrix3fCp: TypeAlias = Union['Matrix3f', '_Array3fCp', '_Matrix3f16Cp']

_Matrix41f16Cp: TypeAlias = Union['Matrix41f16', '_Array41f16Cp']

_Matrix41f64Cp: TypeAlias = Union['Matrix41f64', '_Array41f64Cp', '_Matrix41fCp']

_Matrix41fCp: TypeAlias = Union['Matrix41f', '_Array41fCp', '_Matrix41f16Cp']

_Matrix43f16Cp: TypeAlias = Union['Matrix43f16', '_Array43f16Cp']

_Matrix43f64Cp: TypeAlias = Union['Matrix43f64', '_Array43f64Cp', '_Matrix43fCp']

_Matrix43fCp: TypeAlias = Union['Matrix43f', '_Array43fCp', '_Matrix43f16Cp']

_Matrix44f16Cp: TypeAlias = Union['Matrix44f16', '_Array44f16Cp']

_Matrix44f64Cp: TypeAlias = Union['Matrix44f64', '_Array44f64Cp', '_Matrix44fCp']

_Matrix44fCp: TypeAlias = Union['Matrix44f', '_Array44fCp', '_Matrix44f16Cp']

_Matrix4f16Cp: TypeAlias = Union['Matrix4f16', '_Array4f16Cp']

_Matrix4f64Cp: TypeAlias = Union['Matrix4f64', '_Array4f64Cp', '_Matrix4fCp']

_Matrix4fCp: TypeAlias = Union['Matrix4f', '_Array4fCp', '_Matrix4f16Cp']

_Quaternion4f16Cp: TypeAlias = Union['Quaternion4f16', float]

_Quaternion4f64Cp: TypeAlias = Union['Quaternion4f64', float, '_Quaternion4fCp']

_Quaternion4fCp: TypeAlias = Union['Quaternion4f', float, '_Quaternion4f16Cp']

_TensorXbCp: TypeAlias = Union['TensorXb', bool]

_TensorXf16Cp: TypeAlias = Union['TensorXf16', float, '_TensorXu64Cp']

_TensorXf64Cp: TypeAlias = Union['TensorXf64', float, '_TensorXfCp']

_TensorXfCp: TypeAlias = Union['TensorXf', float, '_TensorXf16Cp']

_TensorXi64Cp: TypeAlias = Union['TensorXi64', int]

_TensorXiCp: TypeAlias = Union['TensorXi', int, '_TensorXbCp']

_TensorXu64Cp: TypeAlias = Union['TensorXu64', int, '_TensorXi64Cp']

_TensorXuCp: TypeAlias = Union['TensorXu', int, '_TensorXiCp']
