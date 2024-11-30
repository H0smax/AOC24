section .data
    message db "Hello world!", 0xA  
    length equ $ - message



section .text
    global _start

_start:
    ; print hello world
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; stdout file descriptor
    mov rsi, message
    mov rdx, length
    syscall

    mov rax, 0x3C
    xor rdi, rdi
    syscall
    

