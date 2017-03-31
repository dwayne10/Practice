    def query(self, queryObject):
        from ._commandUtils import orderByHelper

        def classNameSet(cNames, cFilters):
            x = set([])
            if cNames:
                x.update(cNames.split(','))
            if cFilters:
                x.update(cFilters.split(','))
            return x
        if self._condClass == 'stats':
            if isinstance(queryObject, ClassQuery):
                raise InvalidArgumentException("stats scope is incomplete.")
            mos = self._moDir.query(queryObject)
            if mos:
                self.mos.extend(mos)
            return []

        classNames = getattr(queryObject, 'className', '')
        classFilters = getattr(queryObject, 'classFilter', '')

        if self._condClass == 'aaaSessionLR':
            queryObject.orderBy = 'aaaSessionLR.created|desc'
            propertyFilter = getattr(queryObject, 'propFilter', None)
            if self._filterList:
                r = restFilter(self._condClass, 'and', self._filterList)
                propertyFilter = r[:-1] + ',' + propertyFilter + ')'
            setattr(queryObject, 'propFilter', propertyFilter)
            mos = self._moDir.query(queryObject)
            if mos:
                self.mos.extend(mos)
            return []
        queryObject.orderBy = orderByHelper(self._condClass)
        healthClass = ['healthInst', 'healthRecord']
        if self._condClass not in classNameSet(classNames, classFilters):
            if self._condClass in healthClass:
                subtree = ""
            else:
                subtree = ",subtree"
            subtreeInclude = '{0},{1}'.format(CondMoDirectory.queryClassToIncludeMap[self._condClass],
                                              'no-scoped' + subtree)
            setattr(queryObject, 'subtreeInclude', subtreeInclude)
            setattr(queryObject, 'subtreePropFilter', restFilter(
                self._condClass, 'and', self._filterList))
        else:
            setattr(queryObject, 'propFilter', restFilter(
                self._condClass, 'and', self._filterList))

        mos = self._moDir.query(queryObject)
