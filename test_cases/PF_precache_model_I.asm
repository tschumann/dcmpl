.text:00122840 ; ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦ S U B R O U T I N E ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
.text:00122840
.text:00122840
.text:00122840                 public PF_precache_model_I
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
.text:00122874 ; ---------------------------------------------------------------------------
.text:00122876                 align 10h
.text:00122880
.text:00122880 loc_122880:                             ; CODE XREF: PF_precache_model_I+52j
.text:00122880                 inc     ebx
.text:00122881                 cmp     ebx, 200h
.text:00122887                 jz      short loc_1228B1
.text:00122889
.text:00122889 loc_122889:                             ; CODE XREF: PF_precache_model_I+34j
.text:00122889                                         ; PF_precache_model_I+6Fj
.text:00122889                 mov     eax, dword ptr ds:(sv+30148h)[ebx*4]
.text:00122890                 test    eax, eax
.text:00122892                 jz      short loc_122880
.text:00122894                 mov     [esp+10h+var_C], esi
.text:00122898                 mov     [esp+10h+var_10], eax
.text:0012289B                 call    Q_stricmp
.text:001228A0                 test    eax, eax
.text:001228A2                 jz      loc_12293A
.text:001228A8                 inc     ebx
.text:001228A9                 cmp     ebx, 200h
.text:001228AF                 jnz     short loc_122889
.text:001228B1
.text:001228B1 loc_1228B1:                             ; CODE XREF: PF_precache_model_I+47j
.text:001228B1                 mov     [esp+10h+var_C], esi
.text:001228B5                 mov     [esp+10h+var_10], offset aPf_precache_mo ; "PF_precache_model_I: '%s' Precache can "...
.text:001228BC                 call    Host_Error
.text:001228C1
.text:001228C1 loc_1228C1:                             ; CODE XREF: PF_precache_model_I+30j
.text:001228C1                 xor     ebx, ebx
.text:001228C3                 jmp     short loc_1228E1
.text:001228C3 ; ---------------------------------------------------------------------------
.text:001228C5                 align 4
.text:001228C8
.text:001228C8 loc_1228C8:                             ; CODE XREF: PF_precache_model_I+AAj
.text:001228C8                 mov     [esp+10h+var_C], esi
.text:001228CC                 mov     [esp+10h+var_10], eax
.text:001228CF                 call    Q_stricmp
.text:001228D4                 test    eax, eax
.text:001228D6                 jz      short loc_12293A
.text:001228D8                 inc     ebx
.text:001228D9                 cmp     ebx, 200h
.text:001228DF                 jz      short loc_122943
.text:001228E1
.text:001228E1 loc_1228E1:                             ; CODE XREF: PF_precache_model_I+83j
.text:001228E1                 mov     eax, dword ptr ds:(sv+30148h)[ebx*4]
.text:001228E8                 test    eax, eax
.text:001228EA                 jnz     short loc_1228C8
.text:001228EC                 mov     eax, 1
.text:001228F1                 mov     [esp+10h+var_8], eax
.text:001228F5                 mov     eax, 1
.text:001228FA                 mov     dword ptr ds:(sv+30148h)[ebx*4], esi
.text:00122901                 mov     [esp+10h+var_C], eax
.text:00122905                 mov     [esp+10h+var_10], esi
.text:00122908                 call    Mod_ForName
.text:0012290D                 test    edi, edi
.text:0012290F                 mov     dword ptr ds:(sv+30948h)[ebx*4], eax
.text:00122916                 jnz     short loc_12293A
.text:00122918                 or      ds:(sv+31148h)[ebx], 1
.text:0012291F                 jmp     short loc_12293A
.text:0012291F ; ---------------------------------------------------------------------------
.text:00122921                 align 8
.text:00122928
.text:00122928 loc_122928:                             ; CODE XREF: PF_precache_model_I+17j
.text:00122928                 mov     [esp+10h+var_C], esi
.text:0012292C                 xor     ebx, ebx
.text:0012292E                 mov     [esp+10h+var_10], offset aPf_precache__4 ; "PF_precache_model_I: Bad string '%s'"
.text:00122935                 call    Host_Error
.text:0012293A
.text:0012293A loc_12293A:                             ; CODE XREF: PF_precache_model_I+62j
.text:0012293A                                         ; PF_precache_model_I+96j ...
.text:0012293A                 add     esp, 10h
.text:0012293D                 mov     eax, ebx
.text:0012293F                 pop     ebx
.text:00122940                 pop     esi
.text:00122941                 pop     edi
.text:00122942                 retn
.text:00122943 ; ---------------------------------------------------------------------------
.text:00122943
.text:00122943 loc_122943:                             ; CODE XREF: PF_precache_model_I+9Fj
.text:00122943                 mov     edi, 200h
.text:00122948                 xor     ebx, ebx
.text:0012294A                 mov     [esp+10h+var_8], edi
.text:0012294E                 mov     [esp+10h+var_C], esi
.text:00122952                 mov     [esp+10h+var_10], offset aPf_precache__5 ; "PF_precache_model_I: Model '%s' failed "...
.text:00122959                 call    Host_Error
.text:0012295E                 jmp     short loc_12293A
.text:00122960 ; ---------------------------------------------------------------------------
.text:00122960
.text:00122960 loc_122960:                             ; CODE XREF: PF_precache_model_I+Cj
.text:00122960                 mov     [esp+10h+var_10], offset aPf_precache__6 ; "PF_precache_model_I: NULL pointer"
.text:00122967                 xor     ebx, ebx
.text:00122969                 call    Host_Error
.text:0012296E                 jmp     short loc_12293A
.text:0012296E PF_precache_model_I endp
