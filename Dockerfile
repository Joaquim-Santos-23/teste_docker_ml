FROM continuumio/miniconda3

RUN conda config --add channels conda-forge
RUN conda config --set channel_priority strict
RUN conda update --all
RUN conda create -n ambiente anaconda pip pymysql joblib pandas scipy nltk seaborn matplotlib scikit-learn
RUN conda update -n base -c defaults conda
RUN echo "source activate ambiente" > ~/.bashrc
ENV PATH /opt/conda/envs/ambiente/bin:$PATH

# Copiando projeto para a raíz do conteiner
COPY aplicacao_pca.py /

# Create script for container startup
COPY docker-entrypoint.sh /opt/conda/envs/ambiente/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]