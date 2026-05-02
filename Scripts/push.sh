#!/bin/bash

echo "📤 Subiendo proyecto a GitHub..."

git add .

read -p "📝 Mensaje del commit: " mensaje

git commit -m "$mensaje"

git push

echo "✅ Subido correctamente 🚀"
