class DNAOneTimeTask:

    def run(self):
        self.executor.interaction.activate()
        self.sleep(0.5)
        if self.afk_config.get("鼠标抖动", True):
            self.setup_jitter()
