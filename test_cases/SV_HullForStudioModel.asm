.text:0012A9B0 ; ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦ S U B R O U T I N E ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
.text:0012A9B0
.text:0012A9B0
.text:0012A9B0                 public SV_HullForStudioModel
.text:0012A9B0 SV_HullForStudioModel proc near         ; CODE XREF: SV_SingleClipMoveToEntity+2F6p
.text:0012A9B0
.text:0012A9B0 var_7C          = dword ptr -7Ch
.text:0012A9B0 var_78          = dword ptr -78h
.text:0012A9B0 var_74          = dword ptr -74h
.text:0012A9B0 var_70          = dword ptr -70h
.text:0012A9B0 var_6C          = dword ptr -6Ch
.text:0012A9B0 var_68          = dword ptr -68h
.text:0012A9B0 var_64          = dword ptr -64h
.text:0012A9B0 var_60          = dword ptr -60h
.text:0012A9B0 var_5C          = dword ptr -5Ch
.text:0012A9B0 var_58          = dword ptr -58h
.text:0012A9B0 var_54          = dword ptr -54h
.text:0012A9B0 var_40          = dword ptr -40h
.text:0012A9B0 var_3C          = dword ptr -3Ch
.text:0012A9B0 var_38          = dword ptr -38h
.text:0012A9B0 var_34          = dword ptr -34h
.text:0012A9B0 var_24          = dword ptr -24h
.text:0012A9B0 var_20          = dword ptr -20h
.text:0012A9B0 var_1C          = dword ptr -1Ch
.text:0012A9B0 var_18          = dword ptr -18h
.text:0012A9B0 var_12          = byte ptr -12h
.text:0012A9B0 var_10          = byte ptr -10h
.text:0012A9B0 var_F           = byte ptr -0Fh
.text:0012A9B0 var_E           = dword ptr -0Eh
.text:0012A9B0 arg_0           = dword ptr  14h
.text:0012A9B0 arg_4           = dword ptr  18h
.text:0012A9B0 arg_8           = dword ptr  1Ch
.text:0012A9B0 arg_C           = dword ptr  20h
.text:0012A9B0 arg_10          = dword ptr  24h
.text:0012A9B0
.text:0012A9B0                 push    ebp
.text:0012A9B1                 push    edi
.text:0012A9B2                 push    esi
.text:0012A9B3                 push    ebx
.text:0012A9B4                 sub     esp, 7Ch
.text:0012A9B7                 mov     edi, [esp+7Ch+arg_8]
.text:0012A9BE                 lea     ebp, [esp+7Ch+var_3C]
.text:0012A9C2                 mov     esi, [esp+7Ch+arg_4]
.text:0012A9C9                 mov     ebx, [esp+7Ch+arg_0]
.text:0012A9D0                 fld     dword ptr [edi]
.text:0012A9D2                 fsub    dword ptr [esi]
.text:0012A9D4                 fstp    [esp+7Ch+var_3C]
.text:0012A9D8                 fld     dword ptr [edi+4]
.text:0012A9DB                 fsub    dword ptr [esi+4]
.text:0012A9DE                 fstp    [esp+7Ch+var_38]
.text:0012A9E2                 fld     dword ptr [edi+8]
.text:0012A9E5                 fsub    dword ptr [esi+8]
.text:0012A9E8                 mov     [esp+7Ch+var_78], ebp
.text:0012A9EC                 mov     [esp+7Ch+var_7C], offset vec3_origin
.text:0012A9F3                 fstp    [esp+7Ch+var_34]
.text:0012A9F7                 call    VectorCompare
.text:0012A9FC                 test    eax, eax
.text:0012A9FE                 jz      short loc_12AA20
.text:0012AA00                 test    ds:gGlobalVariables+84h, 1
.text:0012AA07                 jz      loc_12AC00
.text:0012AA0D                 jmp     short loc_12AA20
.text:0012AA0D ; ---------------------------------------------------------------------------
.text:0012AA0F                 align 10h
.text:0012AA10
.text:0012AA10 loc_12AA10:                             ; CODE XREF: SV_HullForStudioModel+269j
.text:0012AA10                 fstp    st
.text:0012AA12                 lea     esi, [esi+0]
.text:0012AA19                 lea     edi, [edi+0]
.text:0012AA20
.text:0012AA20 loc_12AA20:                             ; CODE XREF: SV_HullForStudioModel+4Ej
.text:0012AA20                                         ; SV_HullForStudioModel+5Dj
.text:0012AA20                 xor     eax, eax
.text:0012AA22                 fld     ds:flt_269ED8
.text:0012AA28
.text:0012AA28 loc_12AA28:                             ; CODE XREF: SV_HullForStudioModel+28Fj
.text:0012AA28                                         ; SV_HullForStudioModel+2D8j
.text:0012AA28                 xor     edx, edx
.text:0012AA2A                 cmp     dword ptr [ebx+2B8h], 1
.text:0012AA31                 jz      loc_12AC48
.text:0012AA37
.text:0012AA37 loc_12AA37:                             ; CODE XREF: SV_HullForStudioModel+2A4j
.text:0012AA37                                         ; SV_HullForStudioModel+2B1j ...
.text:0012AA37                 test    al, al
.text:0012AA39                 jnz     short loc_12AA80
.text:0012AA3B                 mov     eax, [ebx+134h]
.text:0012AA41                 mov     eax, dword ptr ds:(sv+30948h)[eax*4]
.text:0012AA48                 test    byte ptr [eax+51h], 2
.text:0012AA4C                 jnz     short loc_12AA80
.text:0012AA4E                 fstp    st
.text:0012AA50                 mov     eax, [esp+7Ch+arg_10]
.text:0012AA57                 mov     dword ptr [eax], 1
.text:0012AA5D                 mov     eax, [esp+7Ch+arg_C]
.text:0012AA64                 mov     [esp+7Ch+var_74], edi
.text:0012AA68                 mov     [esp+7Ch+var_78], esi
.text:0012AA6C                 mov     [esp+7Ch+var_7C], ebx
.text:0012AA6F                 mov     [esp+7Ch+var_70], eax
.text:0012AA73                 call    SV_HullForEntity
.text:0012AA78                 add     esp, 7Ch
.text:0012AA7B                 pop     ebx
.text:0012AA7C                 pop     esi
.text:0012AA7D                 pop     edi
.text:0012AA7E                 pop     ebp
.text:0012AA7F                 retn
.text:0012AA80 ; ---------------------------------------------------------------------------
.text:0012AA80
.text:0012AA80 loc_12AA80:                             ; CODE XREF: SV_HullForStudioModel+89j
.text:0012AA80                                         ; SV_HullForStudioModel+9Cj
.text:0012AA80                 mov     [esp+7Ch+var_40], edx
.text:0012AA84                 fstp    [esp+7Ch+var_78]
.text:0012AA88                 mov     [esp+7Ch+var_74], ebp
.text:0012AA8C                 mov     [esp+7Ch+var_7C], ebp
.text:0012AA8F                 call    VectorScale
.text:0012AA94                 mov     eax, [esp+7Ch+arg_C]
.text:0012AA9B                 mov     dword ptr [eax], 0
.text:0012AAA1                 mov     dword ptr [eax+4], 0
.text:0012AAA8                 mov     dword ptr [eax+8], 0
.text:0012AAAF                 test    byte ptr [ebx+224h], 8
.text:0012AAB6                 mov     edx, [esp+7Ch+var_40]
.text:0012AABA                 jnz     short loc_12AB30
.text:0012AABC                 mov     eax, [esp+7Ch+arg_10]
.text:0012AAC3                 mov     [esp+7Ch+var_54], edx
.text:0012AAC7                 mov     [esp+7Ch+var_58], ebx
.text:0012AACB                 mov     [esp+7Ch+var_68], ebp
.text:0012AACF                 mov     [esp+7Ch+var_5C], eax
.text:0012AAD3                 lea     eax, [ebx+1C0h]
.text:0012AAD9                 mov     [esp+7Ch+var_60], eax
.text:0012AADD                 lea     eax, [ebx+1BCh]
.text:0012AAE3                 mov     [esp+7Ch+var_64], eax
.text:0012AAE7                 lea     eax, [ebx+88h]
.text:0012AAED                 mov     [esp+7Ch+var_6C], eax
.text:0012AAF1                 lea     eax, [ebx+0D0h]
.text:0012AAF7                 mov     [esp+7Ch+var_70], eax
.text:0012AAFB
.text:0012AAFB loc_12AAFB:                             ; CODE XREF: SV_HullForStudioModel+243j
.text:0012AAFB                 mov     eax, [ebx+1A8h]
.text:0012AB01                 mov     [esp+7Ch+var_74], eax
.text:0012AB05                 mov     eax, [ebx+1B0h]
.text:0012AB0B                 mov     [esp+7Ch+var_78], eax
.text:0012AB0F                 mov     eax, [ebx+134h]
.text:0012AB15                 mov     eax, dword ptr ds:(sv+30948h)[eax*4]
.text:0012AB1C                 mov     [esp+7Ch+var_7C], eax
.text:0012AB1F                 call    R_StudioHull
.text:0012AB24                 add     esp, 7Ch
.text:0012AB27                 pop     ebx
.text:0012AB28                 pop     esi
.text:0012AB29                 pop     edi
.text:0012AB2A                 pop     ebp
.text:0012AB2B                 retn
.text:0012AB2B ; ---------------------------------------------------------------------------
.text:0012AB2C                 align 10h
.text:0012AB30
.text:0012AB30 loc_12AB30:                             ; CODE XREF: SV_HullForStudioModel+10Aj
.text:0012AB30                 mov     eax, [ebx+134h]
.text:0012AB36                 mov     eax, dword ptr ds:(sv+30948h)[eax*4]
.text:0012AB3D                 mov     [esp+7Ch+var_7C], eax
.text:0012AB40                 call    Mod_Extradata
.text:0012AB45                 mov     ecx, [ebx+1A8h]
.text:0012AB4B                 lea     esi, [ecx+ecx*4]
.text:0012AB4E                 lea     ecx, [ecx+esi*2]
.text:0012AB51                 mov     edx, [eax+0A8h]
.text:0012AB57                 shl     ecx, 4
.text:0012AB5A                 mov     ds:pstudiohdr, eax
.text:0012AB5F                 lea     esi, [esp+7Ch+var_24]
.text:0012AB63                 add     ecx, edx
.text:0012AB65                 add     ecx, eax
.text:0012AB67                 mov     eax, [ebx+0D0h]
.text:0012AB6D                 mov     [esp+7Ch+var_24], eax
.text:0012AB71                 mov     eax, [ebx+0D4h]
.text:0012AB77                 mov     [esp+7Ch+var_20], eax
.text:0012AB7B                 mov     eax, [ebx+0D8h]
.text:0012AB81                 mov     [esp+7Ch+var_74], esi
.text:0012AB85                 mov     [esp+7Ch+var_7C], ecx
.text:0012AB88                 mov     [esp+7Ch+var_1C], eax
.text:0012AB8C                 lea     eax, [esp+7Ch+var_18]
.text:0012AB90                 mov     [esp+7Ch+var_78], eax
.text:0012AB94                 call    R_StudioPlayerBlend
.text:0012AB99                 mov     eax, [esp+7Ch+var_18]
.text:0012AB9D                 mov     edx, [esp+7Ch+var_40]
.text:0012ABA1                 mov     byte ptr [esp+7Ch+var_E+1], 0
.text:0012ABA6                 mov     [esp+7Ch+var_12], 7Fh
.text:0012ABAB                 mov     byte ptr [esp+7Ch+var_E], al
.text:0012ABAF                 mov     eax, [esp+7Ch+arg_10]
.text:0012ABB6                 mov     byte ptr [esp+6Bh], 7Fh
.text:0012ABBB                 mov     [esp+7Ch+var_10], 7Fh
.text:0012ABC0                 mov     [esp+7Ch+var_F], 7Fh
.text:0012ABC5                 mov     [esp+7Ch+var_5C], eax
.text:0012ABC9                 lea     eax, [esp+7Ch+var_E]
.text:0012ABCD                 mov     [esp+7Ch+var_60], eax
.text:0012ABD1                 lea     eax, [esp+7Ch+var_12]
.text:0012ABD5                 mov     [esp+7Ch+var_64], eax
.text:0012ABD9                 lea     eax, [ebx+88h]
.text:0012ABDF                 mov     [esp+7Ch+var_54], edx
.text:0012ABE3                 mov     [esp+7Ch+var_58], ebx
.text:0012ABE7                 mov     [esp+7Ch+var_68], ebp
.text:0012ABEB                 mov     [esp+7Ch+var_6C], eax
.text:0012ABEF                 mov     [esp+7Ch+var_70], esi
.text:0012ABF3                 jmp     loc_12AAFB
.text:0012ABF3 ; ---------------------------------------------------------------------------
.text:0012ABF8                 align 10h
.text:0012AC00
.text:0012AC00 loc_12AC00:                             ; CODE XREF: SV_HullForStudioModel+57j
.text:0012AC00                 test    byte ptr [ebx+224h], 8
.text:0012AC07                 jz      short loc_12AC80
.text:0012AC09                 fld     sv_clienttrace+0Ch
.text:0012AC0F                 fldz
.text:0012AC11                 fxch    st(1)
.text:0012AC13                 fucomi  st, st(1)
.text:0012AC15                 fstp    st(1)
.text:0012AC17                 jp      short loc_12AC1F
.text:0012AC19                 jz      loc_12AA10
.text:0012AC1F
.text:0012AC1F loc_12AC1F:                             ; CODE XREF: SV_HullForStudioModel+267j
.text:0012AC1F                 fmul    ds:flt_269ED8
.text:0012AC25                 mov     al, 1
.text:0012AC27                 mov     [esp+7Ch+var_34], 3F800000h
.text:0012AC2F                 mov     [esp+7Ch+var_38], 3F800000h
.text:0012AC37                 mov     [esp+7Ch+var_3C], 3F800000h
.text:0012AC3F                 jmp     loc_12AA28
.text:0012AC3F ; ---------------------------------------------------------------------------
.text:0012AC44                 align 8
.text:0012AC48
.text:0012AC48 loc_12AC48:                             ; CODE XREF: SV_HullForStudioModel+81j
.text:0012AC48                 cmp     ds:g_bIsTerrorStrike, 1
.text:0012AC4F                 mov     edx, 1
.text:0012AC54                 jz      loc_12AA37
.text:0012AC5A                 cmp     ds:g_bIsCStrike, 1
.text:0012AC61                 jz      loc_12AA37
.text:0012AC67                 xor     edx, edx
.text:0012AC69                 cmp     ds:g_bIsCZero, 1
.text:0012AC70                 setz    dl
.text:0012AC73                 jmp     loc_12AA37
.text:0012AC73 ; ---------------------------------------------------------------------------
.text:0012AC78                 align 10h
.text:0012AC80
.text:0012AC80 loc_12AC80:                             ; CODE XREF: SV_HullForStudioModel+257j
.text:0012AC80                 mov     al, 1
.text:0012AC82                 fld     ds:flt_269ED8
.text:0012AC88                 jmp     loc_12AA28
.text:0012AC88 SV_HullForStudioModel endp
