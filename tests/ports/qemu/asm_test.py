try:
    import frozen_asm_thumb as frozen_asm
except ImportError:
    try:
        import frozen_asm_rv32 as frozen_asm
    except ImportError:
        # Boards that do not freeze an inline assembler module (those whose
        # target has no .mpy architecture ID) skip this test; anywhere else a
        # missing frozen module is a real failure.
        import sys

        if ((getattr(sys.implementation, "_mpy", 0) >> 10) & 0x0F) != 0:
            raise
        print("SKIP")
        raise SystemExit

print(frozen_asm.asm_add(1, 2))
print(frozen_asm.asm_add1(3))
print(frozen_asm.asm_cast_bool(0), frozen_asm.asm_cast_bool(3))
print(frozen_asm.asm_shift_int(4))
print(frozen_asm.asm_shift_uint(4))
