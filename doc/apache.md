Define SRVROOT "/Apache24"
DocumentRoot "${SRVROOT}/htdocs

DocumentRoot /var/www/html                                                                 
                                                                                                 
      <Directory /var/www>                                                                       
          Options Indexes FollowSymLinks MultiViews                                              
          AllowOverride None                                                                     
          Order allow,deny                                                                       
          allow from all                                                                         
      </Directory>
