pasta="/home/Alt/Imagens/Capturas de tela"

cd "$pasta" || exit

for arquivo in *; do
    if [ -f "$arquivo" ]; then
        rm "$arquivo"
        echo "Arquivo $arquivo deletado"
    fi
done

echo "Todos os arquivos na pasta foram deletados."
