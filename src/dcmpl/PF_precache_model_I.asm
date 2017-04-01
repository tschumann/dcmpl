.text:00122840 PF_precache_model_I proc near           ; DATA XREF: .data:g_engfuncsExportedToDllso
.text:00122840
.text:00122840 var_10          = dword ptr -10h
.text:00122840 var_C           = dword ptr -0Ch
.text:00122840 var_8           = dword ptr -8
.text:00122840 arg_0           = dword ptr  10h
.text:00122840
.text:00122840                 push    edi
.text:00122841                 push    esi
.text:00122842                 push    ebx
.text:00122843                 sub     esp, 10h
.text:00122846                 mov     esi, [esp+10h+arg_0]
.text:0012284A                 test    esi, esi
.text:0012284C                 jz      loc_122960
.text:00122852                 movzx   eax, byte ptr [esi]
.text:00122855                 cmp     al, 20h
.text:00122857                 jle     loc_122928
.text:0012285D                 xor     edi, edi
.text:0012285F                 cmp     al, 21h
.text:00122861                 jnz     short loc_122869
.text:00122863                 inc     esi
.text:00122864                 mov     edi, 1
.text:00122869
.text:00122869 loc_122869:                             ; CODE XREF: PF_precache_model_I+21j
.text:00122869                 cmp     dword ptr ds:sv+3BC64h, 1
.text:00122870                 jz      short loc_1228C1
.text:00122872                 xor     ebx, ebx
.text:00122874                 jmp     short loc_122889
