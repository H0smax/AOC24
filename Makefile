# Nombre de la carpeta se pasa como argumento: make dayN (e.g., make day0)
TARGET_DIR := $(day)

# Ensamblador y enlazador
ASM := nasm
LD := ld

# Flags para ensamblador y enlazador
ASM_FLAGS := -f elf64
LD_FLAGS := -o

# Archivos y salida
ASM_FILES := $(wildcard $(TARGET_DIR)/*.asm)
OBJ_FILES := $(ASM_FILES:.asm=.o)
OUTPUT := $(TARGET_DIR)/output

# Regla principal
all: $(TARGET_DIR)
	@echo "Compilando archivos en $(TARGET_DIR)..."
	$(ASM) $(ASM_FLAGS) $(ASM_FILES) -o $(OBJ_FILES)
	$(LD) $(OBJ_FILES) $(LD_FLAGS) $(OUTPUT)
	@echo "Ejecutable generado: $(OUTPUT)"

# Regla para especificar la carpeta
$(TARGET_DIR):
	@if [ ! -d "$(TARGET_DIR)" ]; then \
		echo "Error: El directorio $(TARGET_DIR) no existe."; \
		exit 1; \
	fi

# Limpiar archivos generados
clean:
	rm -f $(TARGET_DIR)/*.o $(TARGET_DIR)/output
	@echo "Archivos compilados eliminados."
