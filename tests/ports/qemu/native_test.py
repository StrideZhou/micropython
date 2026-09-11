import sys

# Boards whose target has no .mpy architecture ID (AArch64 today, and any board
# without a native emitter) cannot freeze native/viper/inline-asm modules, so
# this test does not apply to them.  Every other board is expected to freeze
# the module, so an ImportError there is still reported as a failure.
NATIVE_MPY_ARCH = (getattr(sys.implementation, "_mpy", 0) >> 10) & 0x0F

try:
    import native_frozen_align
except ImportError:
    if NATIVE_MPY_ARCH != 0:
        raise
    print("SKIP")
    raise SystemExit

native_frozen_align.native_x(1)
native_frozen_align.native_y(2)
native_frozen_align.native_z(3)
