# by just6889
init -999 python:
    import renpy.store as store
    import renpy.exports as renpy
    import os
    import cPickle as pickle
    import zlib

    def migrate_persistent_data(old_persistent):
        """
        Migra el persistente antiguo a la nueva version
        """
        for attr in dir(old_persistent):
            if not attr.startswith('__') and not callable(getattr(old_persistent, attr)):
                setattr(store.persistent, attr, getattr(old_persistent, attr))

    def load_old_persistent(file_path):
        """
        Carga los datos del persistente
        """
        with open(file_path, 'rb') as f:
            data = f.read()
            data = zlib.decompress(data)
            old_persistent = pickle.loads(data)
        
        return old_persistent

    def save_new_persistent():
        """
        Guarda el nuevo persistente
        """
        renpy.save_persistent()

    def migrate_persistent():
        """
        Funcion para migrar el persistente antiguo a la nueva version de renpy
        """
        
        old_persistent_path = os.path.join(renpy.config.savedir, "persistent")
        
        
        if os.path.exists(old_persistent_path):
            
            old_persistent = load_old_persistent(old_persistent_path)
            
            
            migrate_persistent_data(old_persistent)
            
            
            save_new_persistent()


    # just6889: ya es la segunda revision para este archivo
    # y con esto tendria para migrar persistentes de manera automatica
    # en caso de provenir de otras versiones de Ren'Py :D
    migrate_persistent()
